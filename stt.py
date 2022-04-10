import sys
import requests
import pprint
from time import sleep
#from configure import auth_key
# store global constants

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

def convert_speech_to_text(audio_filename):

    auth_key = '42d6ed6bfe044d368b77f35f0b8f11fc'
    headers = {
    "authorization": auth_key,
    "content-type": "application/json"
    }
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'
    
    # make a function to pass the mp3 to the upload endpoint


    # upload our audio file
    upload_response = requests.post(
    upload_endpoint,
    headers=headers, data=read_file(audio_filename)
    )
    print('Audio file uploaded')

    # send a request to transcribe the audio file
    transcript_request = {'audio_url': upload_response.json()['upload_url']}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    print('Transcription Requested')
    pprint.pprint(transcript_response.json())
    # set up polling
    polling_response = requests.get(transcript_endpoint+"/"+transcript_response.json()['id'], headers=headers)
    filename = transcript_response.json()['id'] + '.txt'
    # if our status isn’t complete, sleep and then poll again
    while polling_response.json()['status'] != 'completed':
        sleep(30)
    polling_response = requests.get(transcript_endpoint+"/"+transcript_response.json()['id'], headers=headers)
    print("File is", polling_response.json()['status'])
    with open(filename, 'w') as f:
        f.write(polling_response.json()['text'])
    print('Transcript saved to', filename)

    return polling_response.json()['text']