from api_activity import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}