sudo apt update
sudo apt install python3-pip
pip3 install librosa soundfile faster-whisper
cd whisper_online_server
python3 whisper_online_server.py --host 0.0.0.0 --port 43001 --model large-v2