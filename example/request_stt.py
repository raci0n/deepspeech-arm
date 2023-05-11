import requests

url = 'http://localhost:8082/stt'
fname = 'file.wav'

# Open the wav-file 
with open(fname, 'rb') as f:
    data = f.read() # read

# http request to 'http://localhost:8082/stt'
req = requests.post(url, data=data)
print(req.text) # print the result
