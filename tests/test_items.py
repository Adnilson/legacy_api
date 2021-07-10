import pytest
import json
import vcr

vcr = vcr.VCR(cassette_library_dir='tests/fixtures/cassettes')

def data_length(response_data):
    return len(json.loads(response_data)['data'])

@vcr.use_cassette()
def test_items(client):
    response = client.get('/items')
    response_data = response.data

    assert response.status_code == 200
    assert data_length(response_data) == 100
    assert json.loads(response_data)['metadata']['perPage'] == 100
    assert json.loads(response_data)['metadata']['page'] == 1

@vcr.use_cassette()
def test_items_page_1_and_5_per_page(client):
    response = client.get("/items?perPage=5")
    response_data = response.data

    assert response.status_code == 200
    assert data_length(response_data) == 5
    assert json.loads(response_data)['metadata']['perPage'] == 5
    assert json.loads(response_data)['metadata']['page'] == 1

@vcr.use_cassette()
def test_items_page_34_and_80_per_page(client):
    response = client.get("/items?page=34&perPage=80")
    response_data = response.data

    assert response.status_code == 200
    assert data_length(response_data) == 80
    assert json.loads(response_data)['metadata']['perPage'] == 80
    assert json.loads(response_data)['metadata']['page'] == 34
