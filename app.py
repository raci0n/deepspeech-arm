from threading import Thread
from flask import Flask
from flask import request
from flask import send_file
import json
import os

# For Deepspeech
from deepspeech import Model
import wave
import numpy as np

# Server Config
IP_ADRESS = '0.0.0.0'
PORT = 8082

# Deepspeech Config
MODEL_FILENAME          =   '/app/model/deepspeech.tflite'
SCORER_FILENAME         =   '/app/model/deepspeech.scorer'
FILENAME                =   'temp.wav'



# Define app as Flask-Server-Class
app = Flask(__name__)


# Deepspeech
ds = Model(MODEL_FILENAME)
ds.enableExternalScorer(SCORER_FILENAME)


# Start Deepspeech
def STT_Deepspeech(fname):
    data = wave.open(fname, 'rb')
    frames = data.readframes(data.getnframes())
    audio = np.frombuffer(frames, np.int16)
    return ds.stt(audio)



# request function over http://IP_ADRESS:PORT/stt
@app.route('/stt', methods=['POST', 'OPTIONS'])
def main():
    try:
        #get wav-file for stt
        data = request.get_data()
        with open(FILENAME,'wb') as f:
            f.write(data)


        res = STT_Deepspeech(FILENAME)

        os.remove(FILENAME)
        return { "STATUS":1, "DEEPSPEECH": res}

    except:
        return { "STATUS":-1, "DEEPSPEECH": ""}


# main function
if __name__ == '__main__':
    app.run(host=IP_ADRESS, port=PORT, debug=True)
