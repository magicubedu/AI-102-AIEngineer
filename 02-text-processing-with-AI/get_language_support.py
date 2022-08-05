import requests, json

translator_endpoint = 'https://api.cognitive.microsofttranslator.com'
path = '/languages'
url = translator_endpoint + path

# Build the request
params = {
    'api-version': '3.0',
    'scope':['transliteration']
}

headers = {
'Content-type': 'application/json'
}


body = [{}]

# Send the request and get response
request = requests.get(url, params=params, headers=headers, json=body)
response = request.json()

# Parse JSON array and get language support
print('----- Response ------')
print(json.dumps(response['transliteration']['ja'], indent=4))

