from helpers import *


def test_post_user():
    assert http_methods.post_user().status_code == 201


def test_get_user():
    response = requests.get(base_url+'?'+user_data['email'], headers=headers_with_auth)
    assert response.status_code == 200


def test_put_user():
    assert http_methods.put().status_code == 200


def test_delete_user():
    assert http_methods.delete().status_code == 204
