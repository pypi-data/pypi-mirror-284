SERVER_IP=18.227.228.6
SERVER_PORT=43007
BUFFER_SIZE=65535
SAMPLE_RATE=16000

sox -t coreaudio default -r $SAMPLE_RATE -c 1 -b 16 --input-buffer $BUFFER_SIZE -e signed-integer -B -t raw - | nc $SERVER_IP $SERVER_PORT