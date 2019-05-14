"""
This file is used to test bot post requests
To use it, you must have the actions server and bot running
And execute
$ python3 post.py
"""

import requests
import json

post_url = "http://localhost:5005/webhooks/rest/webhook"

headers = {'content-type': 'application/json'}

params = {
    "message": "estes são meus dados: {'body_temperature':  37, 'age':  39, 'gender': 'f', 'weight': 90, 'glucose': 100, 'height': 1.98, 'blood_pressure': '12/9', 'alergies': 'remedio', 'medication': 'remedio', 'oxygen_level': 'nenhum', 'previous_diseases': 'uma ai'}"
}


r = requests.post(post_url, data=json.dumps(params), headers=headers)

print(r.text)
