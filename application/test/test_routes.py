import pytest
from application import app

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
    
def test_handle_minions_get(client):
    res = client.get('/minions')
    assert res.status_code == 200
