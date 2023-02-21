import requests
import sys
import json
import pytest

sys.path.append(r'C:\Users\PREDATOR\PycharmProjects\REST_API_automation\config.json')
with open(r'C:\Users\PREDATOR\PycharmProjects\REST_API_automation\config.json') as f:
    config = json.load(f)
base_url = config['url']

headers_with_auth = {"Accept": "application/json",
                     "Content-Type": "application/json",
                     "Authorization": "Bearer 9cc3165b8312515b95359fb3795ed73debd79bd2553fe8280f368272b4d62722"}

user_data = {"name": "MisterBaiden", "gender": "male", "email": "robo.kops@3000.com", "status": "active"}

#
# def get_id():
#     response = requests.get(base_url+'?'+user_data['email'], headers=headers_with_auth)
#     user_id = response.json()[0]['id']
#     return user_id


class HttpRequests:

    @staticmethod
    def post_user():
        return requests.post(base_url, json=user_data, headers=headers_with_auth)

    @staticmethod
    def get():
        response = requests.get(base_url+'?'+user_data['email'], headers=headers_with_auth)
        user_id = response.json()[0]['id']
        return user_id

    @staticmethod
    def put():
        return requests.put(base_url + f'/{http_methods.get()}', json={'name': 'MisterZelensky'},  headers=headers_with_auth)

    @staticmethod
    def delete():
        return requests.delete(base_url+f'/{http_methods.get()}', headers=headers_with_auth)


http_methods = HttpRequests()
