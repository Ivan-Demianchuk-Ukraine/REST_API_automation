from helpers import *


def test_post_user():
    assert http_methods.post_user().status_code == 201


def test_get_user():
    assert http_methods.get_user_data().status_code == 200
    assert http_methods.get_user_name() == user['name']
    assert http_methods.get_user_email() == user['email']
    assert http_methods.get_user_gender() == user['gender']
    assert http_methods.get_user_status() == user['status']


def test_put_user():
    assert http_methods.put_name('new_name1').status_code == 200
    assert http_methods.get_user_name() == 'new_name1'


def test_patch_user():
    assert http_methods.patch_name().status_code == 200


def test_delete_user():
    assert http_methods.delete().status_code == 204
    assert http_methods.patch_name().status_code == 404
