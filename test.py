import json
from storage.storage import StorageByZapier

with open('config.json', 'r') as configfile:
    config = json.load(configfile)

test_data = {
    'name': 'value',
    'type': None,
    'alles': 'zusammen'
}

storage = StorageByZapier(auth_key=config['auth_key'])

storage.put(test_data)
a = storage.get()
print(json.dumps(storage.get()))