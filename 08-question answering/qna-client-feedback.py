import requests

endpoint = 'ENDPOINT'
projectName = 'PROJECTNAME'
deploymentName = 'production'
prediction_key = 'KEY'

headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': prediction_key
}

url = f'{endpoint}/language/query-knowledgebases/projects/{projectName}/feedback?api-version=2021-10-01'

myobj = {
        'records': [
                {
                        'userId': '1234',
                        'userQuestion': 'I want to book a hotel',
                        'qnaId': 142
                }
        ]
}

x = requests.post(url, json = myobj, headers=headers)

print(x.text)

