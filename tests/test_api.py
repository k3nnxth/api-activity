from api_activity.app import create_app
import pytest


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
        
def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}