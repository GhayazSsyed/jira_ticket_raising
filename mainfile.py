# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/createJira" , methods = ['POST'])
def createJira():
     
    url = "<YOUR-URL-HERE"
    API_TOKEN = "API-TOKEN-HERE"

    auth = HTTPBasicAuth("GMAIL-HERE",API_TOKEN )
    data = request.get_json()
    if data["comment"]["body"] != "/jira":
            return jsonify({"message": "Ignored. Comment is not /jira."})    

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "Order entry fails when selecting supplier.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10014"
        },
        "project": {
        "key": "MF"
        },

        "summary": "early morning tickett",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0')

