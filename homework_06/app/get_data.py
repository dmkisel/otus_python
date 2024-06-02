import requests
from homework_06.app.models.user import User

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/1"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_users_data():
    url = USERS_DATA_URL
    response = requests.get(url)
    user = User(name=response['name'],
                username=response['username'],
                email=response['email'])
    return user
