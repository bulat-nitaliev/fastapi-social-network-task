import http
import pytest
from sqlalchemy import insert, select
from fastapi import Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import user
from tests.conftest import client


def test_get_user():
    response = client.get('/users/')
    print(response.json())
    assert type(response.json()) == list

def test_get_user_id():
    response_id = client.get('/users/1')
    id = response_id.json()
    assert id[0]['id'] == 1