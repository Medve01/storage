from urllib import response
import requests
import json

class StorageByZapier:
    def __init__(self, auth_key) -> None:
        self.auth_header = auth_header = { "X-Secret": auth_key}
    
    def get(self):
        response = requests.get('https://store.zapier.com/api/records', headers=self.auth_header)
        return json.loads(response.content)

    def put(self,data):
        response = requests.post('https://store.zapier.com/api/records', headers=self.auth_header, data=json.dumps(data))
