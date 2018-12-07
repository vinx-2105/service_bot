import requests
import json

def get_locations():
    url = 'http://127.0.0.1:8000/location_api/location/' 
    data = {'name': "merc", 'path': "LRLRLRLLL"}
    headers = {'content-type': "application/json", "Authorization": "ApiKey admin:12345"}
    post_response = requests.post(url, json.dumps(data), headers = headers)
    response = requests.get('http://127.0.0.1:8000/location_api/location/?format=json&username=admin&api_key=12345')
    result = []
    if(response.status_code==200):
        #successfully fetched locations data
        content = json.loads(response.content.decode("utf-8"))
        for item in content['objects']:
            result.append({'name':item['name'], 'path':item['path']})
        return result
    else:
        return None

get_locations()
