import pytest
from practice_app import app
@pytest.fixture
def client():
    return app.test_client()
def test_page_1(client):
    response=client.get('/')
    assert response.status_code==200
    assert response.data==b'I am in the home page'

def test_page_2(client):
    response=client.get('/new_page')
    assert response.status_code==200
    assert response.data==b'I am in a new page'
