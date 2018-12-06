import requests
import json

def get_orders():
    response = requests.get('http://127.0.0.1:8000/order_api/order/?format=json')
    result = []
    if(response.status_code==200):
        #successfully fetched locations data
        content = json.loads(response.content.decode("utf-8"))
        for item in content['objects']:
            result.append(item)
        return result
    else:
        return None

print(get_orders())