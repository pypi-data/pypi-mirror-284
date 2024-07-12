import argparse
import io
import logging
import os
import socket

import click
import librosa
import numpy as np
import soundfile


from embdata.audio.whisper_online import FasterWhisperASR, asr_factory, load_audio_chunk
from embdata.audio import line_packet

SAMPLING_RATE = 16000


class WhisperServer:
    def __init__(self, **kwargs):
        self.args = argparse.Namespace(**kwargs)
        self.setup_logging()
        self.asr, self.online = self.setup_asr()
        self.asr: FasterWhisperASR = self.asr
        self.min_chunk = self.args.min_chunk_size
        self.warmup()

    def setup_logging(self) -> None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=self.args.log_level, format=log_format)
        self.logger = logging.getLogger(__name__)

    def setup_asr(self):
        return asr_factory(self.args)

    def warmup(self) -> None:
        if self.args.warmup_file and os.path.isfile(self.args.warmup_file):
            a = load_audio_chunk(self.args.warmup_file, 0, 1)
            self.asr.transcribe(a)
            self.logger.info("Whisper is warmed up.")
        else:
            self.logger.warning("Whisper is not warmed up. The first chunk processing may take longer.")

    def start_server(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.args.host, self.args.port))
            s.listen(1)
            self.logger.info(f"Listening on {self.args.host}:{self.args.port}")
            while True:
                conn, addr = s.accept()
                self.logger.info(f"Connected to client on {addr}")
                connection = Connection(conn)
                proc = ServerProcessor(connection, self.online, self.min_chunk, self.logger, self.args.task)
                proc.process()
                conn.close()
                self.logger.info("Connection to client closed")


class Connection:
    PACKET_SIZE = 65536

    def __init__(self, conn):
        self.conn = conn
        self.last_line = ""
        self.conn.setblocking(True)

    def send(self, line) -> None:
        if line != self.last_line:
            line_packet.send_one_line(self.conn, line)
            self.last_line = line

    def receive_lines(self):
        return line_packet.receive_lines(self.conn)

    def non_blocking_receive_audio(self):
        try:
            return self.conn.recv(self.PACKET_SIZE)
        except ConnectionResetError:
            return b""


class ServerProcessor:
    def __init__(self, c, online_asr_proc, min_chunk, logger, task):
        self.connection = c
        self.online_asr_proc = online_asr_proc
        self.min_chunk = min_chunk
        self.logger = logger
        self.task = task
        self.last_end = None

    def receive_audio_chunk(self):
        out = []
        while sum(len(x) for x in out) < self.min_chunk * SAMPLING_RATE:
            raw_bytes = self.connection.non_blocking_receive_audio()
            if not raw_bytes:
                break
            sf = soundfile.SoundFile(
                io.BytesIO(raw_bytes),
                channels=1,
                endian="LITTLE",
                samplerate=SAMPLING_RATE,
                subtype="PCM_16",
                format="RAW",
            )
            audio, _ = librosa.load(sf, sr=SAMPLING_RATE, dtype=np.float32)
            out.append(audio)
        if not out:
            return None
        self.logger.debug("First audio chunk received.")
        return np.concatenate(out)

    def format_output_transcript(self, o) -> str | None:
        if o[0] is not None:
            beg, end = o[0] * 1000, o[1] * 1000
            if self.last_end is not None:
                beg = max(beg, self.last_end)
            self.last_end = end
            return f"{beg:1.0f} {end:1.0f} {o[2]}"
        else:
            return None

    def send_result(self, o) -> None:
        msg = self.format_output_transcript(o)
        if msg is not None:
            self.connection.send(msg)

    def process(self) -> None:
        self.online_asr_proc.init()
        while True:
            a = self.receive_audio_chunk()
            if a is None:
                break
            if self.task == "transcribe":
                self.online_asr_proc.insert_audio_chunk(a)
                o = self.online_asr_proc.process_iter()
            elif self.task == "translate":
                self.online_asr_proc.insert_audio_chunk(a)
                o = self.online_asr_proc.process_iter_translate()
            try:
                self.send_result(o)
            except BrokenPipeError:
                self.logger.info("broken pipe -- connection closed?")
                break
        if self.task == "transcribe":
            o = self.online_asr_proc.finish()
        elif self.task == "translate":
            o = self.online_asr_proc.finish_translate()
        self.send_result(o)


@click.command("whisper")
@click.option("--model", "-m", default="tiny", help="Model size")
@click.option("--lan", "-l", default="auto", help="Language")
@click.option("--min-chunk-size", "-c", default=0.2, help="Minimum chunk size in seconds")
@click.option("--vad", "-v", default=True, help="Enable VAD")
@click.option("--vad-silence-threshold", "-t", default=1.5, help="Silence threshold in seconds")
@click.option("--word-timestamps", "-w", default=True, help="Output word timestamps")
@click.option("--vad-filter", "-f", default=True, help="Filter out non-speech segments")
@click.option("--condition-on-previous-text", "-p", default=True, help="Condition on previous text")
@click.option("--hallucination-threshold", "-h", default=None, help="Hallucination threshold")
@click.option("--log-level", "-l", default="DEBUG", help="Log level")
@click.option("--host", "-o", default="0.0.0.0", help="Host")
@click.option("--port", "-p", default=43007, help="Port")
@click.option("--warmup-file", "-w", default=None, help="Warmup file")
@click.option("--buffer-trimming", "-b", default="segment", help="Buffer trimming strategy")
@click.option("--buffer-trimming-sec", "-s", default=15, help="Buffer trimming length threshold in seconds")
@click.option("--backend", "-b", default="faster-whisper", help="ASR backend")
@click.option("--task", "-t", default="transcribe", help="Task to perform")
@click.option("--model-cache-dir", "-mc", default=None, help="Model cache directory")
@click.option("--model-dir", "-md", default=None, help="Model directory")
@click.option("--save-to-file", "-sf", default=None, help="File to save incoming audio data")
def cli(**kwargs) -> None:
    server = WhisperServer(**kwargs)
    server.start_server()


if __name__ == "__main__":
    cli()
