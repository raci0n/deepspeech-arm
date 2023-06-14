# deepspeech-arm
Its a deepspeech docker container for arm. 

# Installation

Install Raspberry Pi OS [Debian version: **10** (buster), 21.02.2023] on your Raspberry Pi. 

It must be an armv7! Check the version with `uname -a`. Raspberry Pi OS 11 is already on armv8!

Install git:
```
sudo apt install git wget -y

git clone https://github.com/raci0n/deepspeech-arm.git 

cd deepspeech-arm
```

Get your models:

```
wget -O ./model/deepspeech.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
wget -O ./model/deepspeech.tflite https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite

```

Create the docker container:
```
sudo chmod +x ./install.sh
./install.sh
```

Start the docker container:
```
sudo chmod +x ./start.sh
```

The Docker container is now available via `http://localhost:8082`. 

# Example 

```
import requests

url = 'http://localhost:8082/stt'
fname = 'file.wav'

# Open the wav-file 
with open(fname, 'rb') as f:
    data = f.read() # read

# http request to 'http://localhost:8082/stt'
req = requests.post(url, data=data)
print(req.text) # print the result
```

