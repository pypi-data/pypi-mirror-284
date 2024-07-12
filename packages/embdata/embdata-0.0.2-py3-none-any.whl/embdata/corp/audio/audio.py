import numpy as np
import logging
import torch
from transformers import AutoProcessor
from transformers import pipeline
import gradio as gr
import os
import traceback
from functools import partial
import os
from time import time
import traceback
import logging
from typing import Generator, Optional
from dotenv import load_dotenv

import gradio as gr
import numpy as np
import torch
from openai import OpenAI
from transformers import (
    AutoModelForSpeechSeq2Seq,
    AutoProcessor,
    GroundingDinoForObjectDetection,
    pipeline,
)
from PIL import Image as PILImage


load_dotenv()


device = "cuda:7" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
from mbodied.agents import LanguageAgent
from mbodied.types.sense.vision import Image as MBImage

CUSTOM_CSS = """
#footer {display: none !important;}
"""
THEME = gr.themes.Soft(
    primary_hue="red",
    secondary_hue="stone",
    neutral_hue="zinc",
    font_mono=["IBM Plex Mono", "ui-monospace", "Consolas", "monospace"],
)

MODELS = {
    "distil-whisper": {
        "model_id": "distil-whisper/distil-large-v3",
        "model": None,
        "processor": None,
        "pipeline": None,
    },
    "tiny_whisper": {"model_id": "openai/whisper-tiny", "model": None, "processor": None, "pipeline": None},
    "whisper-large-v3": {
        "model_id": "openai/whisper-large-v3",
        "model": None,
        "processor": None,
        "pipeline": None,
    },
}

LANGUAGE_AGENTS = {
    "Claude-Sonnet-3-5": LanguageAgent(model_src="anthropic", api_key=os.getenv("ANTHROPIC_API_KEY")),
    "GPT-4": LanguageAgent(model_src="openai", api_key=os.getenv("OPENAI_API_KEY")),
    "Mistral-7B-instruct-v3": None,
    "Idefics2": None,
    "Phi-3-vision": None,
    "Llava-v1.6-mistral": None,
}

LANG_AGENT = LANGUAGE_AGENTS.get("Claude-Sonnet-3-5")
CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_model(model_name):
    global LANG_AGENT
    if model_name not in MODELS:
        raise ValueError(f"Unknown model: {model_name}")

    if MODELS[model_name]["model"] is None:
        model_id = MODELS[model_name]["model_id"]
        MODELS[model_name]["model"] = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        MODELS[model_name]["model"].to(device)
        MODELS[model_name]["processor"] = AutoProcessor.from_pretrained(model_id)
        MODELS[model_name]["pipeline"] = pipeline(
            "automatic-speech-recognition",
            model=MODELS[model_name]["model"],
            tokenizer=MODELS[model_name]["processor"].tokenizer,
            feature_extractor=MODELS[model_name]["processor"].feature_extractor,
            max_new_tokens=64,
            torch_dtype=torch_dtype,
            device=device,
        )
    LANG_AGENT = LANGUAGE_AGENTS.get(model_name, LANG_AGENT)


PROCESSING_TEXT = "Wait a sec. Processing..."
LAST_TEXT = ""
LAST_TEXT_TIME = 0

PROCESSED_TEXTS = []
PROCESSING = False
LAST_PROCESSED_TEXT = ""


def process_text(text: str, language_model: str) -> Generator[tuple[str, bytes], None, None]:
    global PROCESSING
    if PROCESSING or text.strip() == "" or text.strip().lower() == PROCESSING_TEXT.lower():
        yield "", None
        return
    if "robot" not in text.lower():
        yield "", None
        return

    if not text.endswith(".") and not text.endswith("?") and not text.endswith("!"):
        yield "", None
        return

    if len(text.strip().split()) < 3:
        yield "", None
        return

    global LAST_PROCESSED_TEXT
    if text == LAST_PROCESSED_TEXT or text in LAST_PROCESSED_TEXT or text in PROCESSED_TEXTS:
        yield "", None
        return

    print(f"Processing text: {text}")
    LAST_PROCESSED_TEXT = text
    PROCESSED_TEXTS.append(text)
    PROCESSING = True

    global LANG_AGENT
    if LANG_AGENT is None:
        yield f"Language model {language_model} is not implemented yet.", None
        return

    answer_generator = LANG_AGENT.act(text)

    full_answer = ""
    for answer_chunk in [answer_generator]:
        full_answer += answer_chunk
        try:
            with CLIENT.audio.with_streaming_response.speech.create(
                model="tts-1",
                voice="onyx",
                input=answer_chunk,
            ) as response:
                for audio_chunk in response.iter_bytes():
                    yield full_answer, audio_chunk

            PROCESSING = False
        except Exception as e:
            traceback.print_exc()
            yield full_answer, None
            PROCESSING = False


def transcribe(stream: np.ndarray, new_chunk, model_name: str) -> Generator[tuple[np.ndarray, str], None, None]:
    if new_chunk is None:
        yield stream, ""
        return

    try:
        load_model(model_name)
    except ValueError as e:
        yield stream, str(e)
        return
    except Exception as e:
        traceback.print_exc()
        yield stream, f"An unexpected error occurred: {str(e)}"
        return

    sr, y = new_chunk
    y_mono: np.ndarray = np.mean(y, axis=1) if len(y.shape) > 1 and y.shape[1] > 1 else y
    y_mono = y_mono.astype(np.float32)
    y_mono /= np.max(np.abs(y_mono))

    stream = np.concatenate([stream[-10:], y_mono]) if stream is not None and len(stream) > 0 else y_mono
    chunks = MODELS[model_name]["pipeline"]({"sampling_rate": sr, "raw": stream})["text"]
    result = ""
    for chunk in chunks:
        result += chunk
        print(f"Transcribed: {result}")
        yield stream, result


def ensure_text(stream, text: Optional[str]) -> str:
    global LAST_TEXT
    global LAST_TEXT_TIME
    global PROCESSING

    if PROCESSING:
        return stream, PROCESSING_TEXT

    if "!!" in text:  # Rest the stream
        return [], LAST_TEXT

    return stream, text

    if text is None or text.strip() == LAST_TEXT or len(text.split()) < 3:
        return stream, LAST_TEXT
    if text.strip() == "" or "thank you" in text.lower():
        return stream, LAST_TEXT

    LAST_TEXT_TIME = time()
    LAST_TEXT = text.strip()
    return stream, LAST_TEXT


with gr.Blocks(css=CUSTOM_CSS, theme=THEME) as demo:
    gr.Markdown(
        """
        # You Must Say 'Robot' to Activate the AI
        
        Select your preferred models for speech recognition and language generation below.
        You can also upload or paste an image for image-based queries.
        """
    )

    audio_model = gr.Dropdown(choices=list(MODELS.keys()), label="Select Audio Model:", value="distil-whisper")

    language_model = gr.Dropdown(
        choices=list(LANGUAGE_AGENTS.keys()), label="Select Language Model:", value="Claude-Sonnet-3-5"
    )

    input_audio = gr.Audio(sources=["microphone"], streaming=True)
    # input_image = gr.Image(label="Upload or paste an image (optional)")
    raw_text = gr.Text(label=None, visible=False)
    transcribed_text = gr.Text(label="Transcribed text")
    answer_text = gr.Text(label=None)
    output_audio = gr.Audio(streaming=True, autoplay=True, label="AI voice response")
    stream = gr.State([])

    input_audio.stream(
        transcribe, inputs=[stream, input_audio, audio_model], outputs=[stream, raw_text], trigger_mode="always_last"
    )
    raw_text.change(
        ensure_text, inputs=[stream, raw_text], outputs=[stream, transcribed_text], trigger_mode="always_last"
    )
    transcribed_text.change(
        process_text,
        inputs=[transcribed_text, language_model],
        outputs=[answer_text, output_audio],
        trigger_mode="always_last",
    )

    stop_button = gr.Button("Stop")
    stop_button.click(
        cancels=[input_audio, transcribed_text, answer_text, output_audio],
        inputs=[stream],
        outputs=[stream],
    )

if __name__ == "__main__":
    demo.queue()
    demo.launch(
        show_error=True, server_name="0.0.0.0", share=False, server_port=5003, ssl_verify=False, root_path="/audio"
    )
