import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido' in response.data


def test_hello_default(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hola, mundo!' in response.data


def test_hello_with_name(client):
    response = client.get('/hello?name=test')
    assert response.status_code == 200
    assert b'Hola, test!' in response.data


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}
