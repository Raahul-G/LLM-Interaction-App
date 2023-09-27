import os
from dotenv import load_dotenv, find_dotenv
import requests, json

_ = load_dotenv(find_dotenv()) 

api_key = os.environ['API_KEY']

def get_completion(inputs, parameters=None, ENDPOINT_URL=os.environ['API_BASE']): 
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = { "inputs": inputs }
    if parameters is not None:
        data.update({"parameters": parameters})
    response = requests.request("POST",
                                ENDPOINT_URL,
                                headers=headers,
                                data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))