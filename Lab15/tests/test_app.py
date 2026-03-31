"""
George Athanasopoulos
March 31, 2026
Lab 15, RESTAPIs unit testing
"""

# set up a reusable component using pytest fixture

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True # enables testing mode in your Flask app
    
    # create a Flask test client
    with app.test_client() as client:
        yield client # provides the client object to the test

# test homepage
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

# testing POST request
# CREATE ITEM 

def test_create_item(client):
    response = client.post('/items', json = {'name' : 'Book', 'price' : 10})

    assert response.status_code == 201
    data = response.get_json()

    assert 'id' in data
    assert data['item']['name'] == 'Book'
    assert data['item']['price'] == 10

# --------------------------------------
# TESTING GET 
# --------------------------------------
# Read single item
def test_get_single_item(client):
    client.post('/items', json = {'name' : 'Laptop', 'price' : 980})

    response = client.get('/items/2')

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Laptop'

# Read all items
def test_get_items(client):
    client.post('/items', json = {'name' : 'Bookbag', 'price' : 130})

    response = client.get('/items')

    assert response.status_code == 200
    data = response.get_json()

    assert len(data) == 3

# --------------------------------------
# TESTING PUT (update)     
# --------------------------------------
def test_update_item(client):
    response = client.put('/items/3', json = {'name' : 'phone'})
    
    assert response.status_code == 200
    get_all = client.get('/items')
    data = get_all.get_json()
    assert data['3']['name'] == 'phone'

# --------------------------------------
# TESTING DELETE 
# --------------------------------------
def test_delete_item(client):
    response = client.delete('/items/1')

    assert response.status_code == 200
    get_all = client.get('/items').get_json()
    assert '1' not in get_all