from httpx import AsyncClient
from tests.conftest import client


def test_add_post():
    response = client.post("/auth/register", json={
    "email": "string@gmail.com",
    "password": "string",
    "is_active": True,
    "is_superuser": False,
    "is_verified": False,
    "username": "string"
    })
    data = {"username": "string@gmail.com", "password": "string"}
    response_login = client.post('/auth/jwt/login',data=data)
    token = response_login.json()['access_token']
    response = client.post("/posts", json={
        "title": "string",
        "content": "string",
        "date_creation": "2023-09-04T12:22:16.719"}, 
        headers={'Authorization': 'Bearer ' + token})
        
    assert response.json()=={'status': 'success'}

def test_get_post():
    responce = client.get('/posts/')

    assert responce.status_code == 200