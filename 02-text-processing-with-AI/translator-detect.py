import requests, json
from dotenv import load_dotenv
import os

# Get Configuration Settings
load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')
translator_endpoint = ''

# Use the Translator detect function
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

# Parse JSON array and get language
print('----- Response ------')
print(response)
print('----- Language ------')
language = response[0]["language"]
print(language)
