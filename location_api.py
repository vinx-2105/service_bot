import requests
import json

def get_locations():
    response = requests.get('http://127.0.0.1:8000/location_api/location/?format=json')
    result = []
    if(response.status_code==200):
        #successfully fetched locations data
        content = json.loads(response.content.decode("utf-8"))
        for item in content['objects']:
            result.append({'name':item['name'], 'path':item['path']})
        return result
    else:
        return None