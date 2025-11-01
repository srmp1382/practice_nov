import pytest
from practice_app import app
@pytest.fixture()
def client(app):
    return app.test_client()
def page_1():
    response=client.get('/')
   
    assert response.data=='I am in the home page'
def page_2():
    response=client.get('/new_page')

    assert response.data=='I am in a new page'