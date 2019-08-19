import requests

json={
    'month': 'May',
    'result': '1:0',
    'team': 'Manchester',
}

url='https://enz3jynlhy0qi.x.pipedream.net'
# url='http://requestb.in/1h702go1'

response=requests.post(url, json=json, data='Hi')
print(response.status_code)