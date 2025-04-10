import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")

def get_comments_by_post(post_id):
    return requests.get(f"{BASE_URL}/comments", params={"postId": post_id})

def post_post(data):
    return requests.post(f"{BASE_URL}/posts", json=data)

def put_post(post_id, data):
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=data)

def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")
