import requests
import json
from random import randint


with open(r'config.json') as f:
    config = json.load(f)
base_url = config['url']

with open(r'data.json') as f2:
    json_data = json.load(f2)
user = json_data['user_1']

headers_with_auth = {"Accept": "application/json",
                     "Content-Type": "application/json",
                     "Authorization": "Bearer 9cc3165b8312515b95359fb3795ed73debd79bd2553fe8280f368272b4d62722"}


random_name = None


def generate_random():
    global random_name
    random_value = str(randint(1, 999999999))
    return random_value


class HttpRequests:

    @staticmethod
    def post_user():
        return requests.post(base_url, json=user, headers=headers_with_auth)

    @staticmethod
    def get_user_id():
        response = requests.get(base_url+'?'+user['email'], headers=headers_with_auth)
        if user['email'] == response.json()[0]['email']:
            user_id = response.json()[0]['id']
            return user_id
        else:
            pass

    @staticmethod
    def get_user_name():
        response = requests.get(base_url + f'/{http_methods.get_user_id()}', headers=headers_with_auth)
        user_name = response.json()['name']
        return user_name

    @staticmethod
    def get_user_email():
        response = requests.get(base_url + f'/{http_methods.get_user_id()}', headers=headers_with_auth)
        user_email = response.json()['email']
        return user_email

    @staticmethod
    def get_user_gender():
        response = requests.get(base_url + f'/{http_methods.get_user_id()}', headers=headers_with_auth)
        user_gender = response.json()['gender']
        return user_gender

    @staticmethod
    def get_user_status():
        response = requests.get(base_url + f'/{http_methods.get_user_id()}', headers=headers_with_auth)
        user_status = response.json()['status']
        return user_status

    @staticmethod
    def get_user_data():
        return requests.get(base_url + f'/{http_methods.get_user_id()}', headers=headers_with_auth)

    @staticmethod
    def put_name(value: str):
            return requests.put(base_url + f'/{http_methods.get_user_id()}', json={'name': value},
                                headers=headers_with_auth)

    @staticmethod
    def patch_name(value: str):
        return requests.patch(base_url + f'/{http_methods.get_user_id()}', json={'name': value},
                              headers=headers_with_auth)

    @staticmethod
    def delete():
        return requests.delete(base_url+f'/{http_methods.get_user_id()}', headers=headers_with_auth)


http_methods = HttpRequests()
