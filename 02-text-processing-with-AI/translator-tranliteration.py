import requests, json
from dotenv import load_dotenv
import os

# Get Configuration Settings
load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')
translator_endpoint = 'https://api.cognitive.microsofttranslator.com'

# Use the Translator transliteration function
path = '/transliterate'
url = translator_endpoint + path

# Build the request
params = {
    'api-version': '3.0',
    'language':'ja',
    'fromScript':'Jpan',
    'toScript':'Latn'
}

headers = {
'Ocp-Apim-Subscription-Key': cog_key,
'Ocp-Apim-Subscription-Region': cog_region,
'Content-type': 'application/json'
}

text = '私はバスで学校へ行きます'

body = [{
    'text': text
}]

# Send the request and get response
request = requests.post(url, params=params, headers=headers, json=body)
response = request.json()

# Parse JSON array and get translated text
print('----- Response ------')
print(response)
print('----- Original text ------')
print(text)
print('----- Translated text ------')
transliteration = response[0]["text"]
print(transliteration)