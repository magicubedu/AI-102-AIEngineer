import requests, json
from dotenv import load_dotenv
import os

# Get Configuration Settings
load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')
translator_endpoint = 'https://api.cognitive.microsofttranslator.com'

# Use the Translator translate function
path = ''
url = translator_endpoint + path

# Build the request
params = {
    'api-version': '3.0'
}

headers = {
'Ocp-Apim-Subscription-Key': cog_key,
'Ocp-Apim-Subscription-Region': cog_region,
'Content-type': 'application/json'
}

text = 'hello. welcome to una'

body = [{
    'text': text
}]

# Send the request and get response
request = requests.post(url, params=params, headers=headers, json=body)
response = request.json()

# Parse JSON array and get translated text
print('----- Response ------')
print(response)
print('----- Translated text ------')
translation = response[0]["translations"][0]["text"]
print(translation)