import pytest
import logging
from apis.json_api import get_post, get_user, get_comments_by_post
from apis.json_api import post_post, put_post, delete_post


def test_get_post_success():
    res = get_post(1)
    logging.info(f"Response: {res.json()}")
    assert res.status_code == 200
    assert "userId" in res.json()

def test_get_user_success():
    res = get_user(1)
    logging.info(f"Response: {res.json()}")
    assert res.status_code == 200
    assert res.json()["id"] == 1

@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_comments(post_id):
    res = get_comments_by_post(post_id)
    logging.info(f"Comments for post {post_id}: {res.json()}")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_post_not_found():
    res = get_post(99999)
    assert res.status_code == 404

def test_create_post():
    data = {
        "title": "test post",
        "body": "This is a test post",
        "userId": 1
    }
    res = post_post(data)
    assert res.status_code == 201
    assert res.json()["title"] == "test post"

def test_update_post():
    data = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    res = put_post(1, data)
    assert res.status_code == 200
    assert res.json()["title"] == "updated title"

def test_delete_post():
    res = delete_post(1)
    assert res.status_code == 200
def test_create_post():
    data = {
        "title": "test post",
        "body": "This is a test post",
        "userId": 1
    }
    res = post_post(data)
    assert res.status_code == 201
    assert res.json()["title"] == "test post"

def test_update_post():
    data = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    res = put_post(1, data)
    assert res.status_code == 200
    assert res.json()["title"] == "updated title"

def test_delete_post():
    res = delete_post(1)
    assert res.status_code == 200
