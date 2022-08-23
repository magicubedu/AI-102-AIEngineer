import requests

endpoint = 'ENDPOINT'
projectName = 'PROJECTNAME'
deploymentName = 'production'
prediction_key = 'KEY'

headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': prediction_key
}


url = f'{endpoint}/language/:query-knowledgebases?projectName={projectName}&deploymentName={deploymentName}&api-version=2021-10-01'

text = input('>>>> input: ')
myobj = {
        'top': 3,
        'question': text,
}

x = requests.post(url, json = myobj, headers=headers)

print(x.text)

