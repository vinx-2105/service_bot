import requests
import json

def get_orders():
    """
    url = 'http://127.0.0.1:8000/order_api/order/' 
    data = {'source': "merc", 'destination': "jupiter"}
    headers = {'content-type': "application/json", "Authorization": "ApiKey admin:12345"}
    resp = requests.post(url, json.dumps(data), headers = headers)
    if(resp.status_code!=200):
         print("sssssssss      "+str(resp.status_code))
    """
    response = requests.get('http://192.168.43.125:8000/order_api/order/?format=json&username=admin&api_key=12345')
    result = []
    if(response.status_code==200):
        #successfully fetched locations data
        content = json.loads(response.content.decode("utf-8"))
        for item in content['objects']:
            result.append(item)
        return result
    else:
        return None


