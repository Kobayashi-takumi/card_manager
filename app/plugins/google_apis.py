import base64
import requests
import json


def detect_text(import_file, access_token=None):

    base64_image = base64.b64encode(import_file.read()).decode()

    url = 'https://vision.googleapis.com/v1/images:annotate'
    header = {'Content_Type': 'application/json'}
    img_requests = []

    img_requests.append({
        'image': {
            'content': base64_image,
        },
        'features': [{
            'type': 'TEXT_DETECTION',
            'maxResults': 1,
        }]
    })
    response = requests.post(url,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': access_token},
                             headers=header)

    text = response.json()['responses'][0]['textAnnotations'][0]['description']
    text_list = text.splitlines(True)

    return text_list


def extract_entities(text_list, access_token=None):

    url = 'https://language.googleapis.com/v1beta1/documents:analyzeEntities?key={}'.format(access_token)
    header = {'Content-Type': 'application/json'}
    results = []

    for text in text_list:
        body = {
            "document": {
                "type": 'PLAIN_TEXT',
                "language": "JA",
                "content": text
            },
            "encodingType": 'UTF8'
        }
        response = requests.post(url, headers=header, json=body).json()
        results.append(response)
    return response


def extract_required_entities(text, access_token=None):
    entities = extract_entities(text, access_token)
    required_entities = {'ORGANIZATION': '', 'PERSON': '', 'LOCATION': ''}
    for entity in entities['entities']:
        label = entity['type']
        if label in required_entities:
            required_entities[label] += entity['name']

    return required_entities
