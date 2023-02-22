from helpers import *


def test_post_user():
    """
    1. Create user_1
    Expected:
        - user_1 is created
        - status code 201 is received.
    """
    assert http_methods.post_user().status_code == 201


def test_get_user():
    """
    1. Get all data from user_1
    2. Get 'username' value of user_1
    3. Get 'email' value of user_1
    4. Get 'gender' value of user_1
    5. Get 'status' value of user_1
    Expected:
        - status code is 200
        - username has all values that configured in the data.json for user_1
    """
    assert http_methods.get_user_data().status_code == 200
    assert http_methods.get_user_name() == user['name']
    assert http_methods.get_user_email() == user['email']
    assert http_methods.get_user_gender() == user['gender']
    assert http_methods.get_user_status() == user['status']


def test_put_user():
    """
    1. Update name for user_1 via put method
    2. Get new 'username'

    Expected:
        - status code is 200
        - username was changed on new
    """
    global random_name
    random_name = generate_random()
    assert http_methods.put_name(random_name).status_code == 200
    assert http_methods.get_user_name() == random_name


def test_patch_user():
    """
    1. Update name for user_1 via patch method
    2. Get new 'username'

    Expected:
        - status code is 200
        - username was changed on 'patch_new_name'
    """
    global random_name
    random_name = generate_random()
    assert http_methods.patch_name(random_name).status_code == 200
    assert http_methods.get_user_name() == random_name


def test_delete_user():
    """
    1. Delete user_1

    Expected:
        - status code is 204
        - user_1 was deleted
    """
    assert http_methods.delete().status_code == 204
    assert http_methods.patch_name(random_name).status_code == 404
