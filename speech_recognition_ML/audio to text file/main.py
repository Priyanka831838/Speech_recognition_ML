import requests
from api_02 import *

filename = "harvard.wav"
audio_url = upload(filename)

save_transcript(audio_url, "file_title")
