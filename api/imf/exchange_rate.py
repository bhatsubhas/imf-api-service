import requests
from werkzeug.wrappers import Response
from . import imf_api

BASE_URL = "https://www.imf.org/external/np/fin/data/"


@imf_api.get("/lastFiveDays")
def get_last_five_days():
    endpoint_url = BASE_URL + "rms_five.aspx"
    resp = requests.get(endpoint_url, [("tsvflag", "Y")])
    return Response(resp, status=200)


@imf_api.get("/monthly/<string:select_date>")
def get_monthly(select_date):
    endpoint_url = BASE_URL + "rms_mth.aspx"
    params = [
        ("SelectDate", f"{select_date}"),
        ("reportType", "SDRCV"),
        ("tsvflag", "Y"),
    ]
    resp = requests.get(endpoint_url, params=params)
    return Response(resp, status=200)
