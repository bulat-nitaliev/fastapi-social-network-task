import http
import pytest
from sqlalchemy import insert, select
from fastapi import Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from tests.conftest import client



def test_register():
    response = client.post("/auth/register", json={
    "email": "string",
    "password": "string",
    "is_active": True,
    "is_superuser": False,
    "is_verified": False,
    "username": "string"
    })
    print(response.json())
    assert response.status_code == 201
   

def test_login():
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
    assert response_login.status_code == 200
    
    response = client.post("/posts", json={
        "title": "string",
        "content": "string",
        "date_creation": "2023-09-04T12:22:16.719"
    }, headers={'Authorization': 'Bearer ' + token})
    
     
    assert response.json()=={'status': 'success'}