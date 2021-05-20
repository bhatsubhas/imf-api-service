from datetime import datetime, date
from . import client

URL_PREFIX = "/api/v1/exchangeRate"


def test_health_endpoint(client):
    """
    Check if the serivce has health endpoint.

    This endpoint checks if service is running healthy or not
    """
    resp = client.get(f"{URL_PREFIX}/health")
    json_data = resp.get_json()
    assert 200 == resp.status_code
    assert "Service status is healthy" in json_data["message"]


def test_exchangeRate_lastFiveDays(client):
    """
    Check if endpoint to get last five days exchange rates is available.

    Endpoint checks if service returns proper data from IMF Website.
    """
    resp = client.get(f"{URL_PREFIX}/lastFiveDays")
    assert 200 == resp.status_code
    assert b"last five days" in resp.data


def test_exchangeRate_monthly_current_date(client):
    """
    Check if endpoint to get given months exchange rates is available.

    Endpoint checks if service returns proper data form IMF Website.
    """
    current_date = datetime.now()
    select_date = current_date.strftime("%Y-%m-%d")
    month_year = current_date.strftime("%B %Y")

    resp = client.get(f"{URL_PREFIX}/monthly/{select_date}")
    assert 200 == resp.status_code

    expected = bytes(f"SDRs per Currency unit for {month_year}", "utf-8")
    assert expected in resp.data


def test_exchangeRate_monthly_last_month_date(client):
    """
    Check if endpoint to get given months exchange rates is available.

    Endpoint checks if service returns proper data form IMF Website.
    """
    current_date = datetime.today()
    previous_month_date = date(
        current_date.year, current_date.month - 1, 1)
    previous_month_year = previous_month_date.strftime("%B %Y")

    resp = client.get(f"{URL_PREFIX}/monthly/{previous_month_date}")
    assert 200 == resp.status_code

    message = f"SDRs per Currency unit for {previous_month_year}"
    expected = bytes(message, "utf-8")
    assert expected in resp.data


def test_exchangeRate_monthly_no_date(client):
    """
    Check if endpoint to get given months exchange rates is available.

    Endpoint checks if service returns proper data form IMF Website.
    """
    resp = client.get(f"{URL_PREFIX}/monthly")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert "Resource not found" in json_data["Error"]


def test_404_error(client):
    """
    Check if service throws 404 error when unknown resource is requested.
    """
    resp = client.get("/api/v1/unknownResource")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert "Resource not found" in json_data["Error"]
