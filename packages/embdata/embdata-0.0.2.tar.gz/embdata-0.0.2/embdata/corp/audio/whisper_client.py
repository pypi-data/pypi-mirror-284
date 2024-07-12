import argparse
import contextlib
import socket
import threading

import sounddevice as sd

SAMPLING_RATE = 16000
PACKET_SIZE = 1024  # Size of each packet to send


def audio_callback(indata, frames, time, status) -> None:
    """Callback function to capture audio and send it to the server."""
    if status:
        pass
    audio_data = indata.tobytes()
    with contextlib.suppress(Exception):
        sock.sendall(audio_data)


def receive_translations() -> None:
    """Function to receive and print translations from the server."""
    last_translation = ""
    while True:
        try:
            data = sock.recv(1024).decode("utf-8")
            if data and data != last_translation:
                last_translation = data
        except ConnectionResetError:
            break
        except Exception:
            pass


def main(server_ip, server_port) -> None:
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))

    # Start a thread to receive translations
    threading.Thread(target=receive_translations, daemon=True).start()

    try:
        # Open the audio stream
        with sd.InputStream(samplerate=SAMPLING_RATE, channels=1, dtype="int16", callback=audio_callback):
            while True:
                sd.sleep(1000)
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stream audio from the microphone to a server.")
    parser.add_argument("--host", default="18.227.228.6", type=str, help="Server IP address")
    parser.add_argument("--port", default="43007", type=int, help="Server port")
    args = parser.parse_args()

    main(args.host, args.port)
