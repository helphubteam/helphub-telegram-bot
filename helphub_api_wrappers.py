import json
import requests
import os
AUTH_API_ENDPOINT = os.environ['AUTH_API_ENDPOINT']
REQ_API_ENDPOINT = os.environ['REQ_API_ENDPOINT']

def do_auth(username, password, url=AUTH_API_ENDPOINT):

    try:
        r = requests.post(url=url, data={"email":username,"password":password},timeout=2)
        return json.loads(r.text)
    except:
        return False

def get_reqs(token, url=REQ_API_ENDPOINT):
    try:
        r = requests.get(url=url, headers={"Authorization":"Bearer "+token},timeout=2)
        r.raise_for_status()
        reqs=json.loads(r.text)
        for req in reqs:
            for _key in ['title','comment','state','creator_phone']:
                if req[_key] is None: req[_key] =""
        return reqs
    except:
        return False