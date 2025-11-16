def test_health_endpoint(client):
    """
    Check if the serivce has health endpoint.

    This endpoint checks if service is running healthy or not
    """
    resp = client.get("/health")
    json_data = resp.get_json()
    assert 200 == resp.status_code
    assert "Service status is healthy" in json_data["message"]


def test_404_error(client):
    """
    Check if service throws 404 error when unknown resource is requested.
    """
    resp = client.get("/api/v1/unknownResource")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert "Resource not found" in json_data["error"]
