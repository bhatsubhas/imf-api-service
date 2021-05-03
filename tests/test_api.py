import pytest
from imfapi.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    '''
    Check if the serivce has health endpoint. 

    This endpoint checks if service is running healthy or not
    '''
    resp = client.get('/api/v1/health')
    json_data = resp.get_json()
    assert 200 == resp.status_code
    assert 'Service status is healthy' in json_data['message']


def test_exchangeRate_endpoint(client):
    '''
    Check if the service has exchangeRate endpoint. 

    This endpoint checks if service returns proper data from IMF Exchane Rate Endpoing
    '''
    resp = client.get('/api/v1/exchangeRate')
    assert 200 == resp.status_code
    assert b'last five days' in resp.data


def test_404_error(client):
    '''
    Check if service throws 404 error when unknown resource is requested.
    '''

    resp = client.get('/api/v1/unknownResource')
    json_data = resp.get_json()
    assert 404 == resp.status_code
    assert 'The requested URL was not found on the server.' in json_data['message']
