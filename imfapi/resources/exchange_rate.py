from flask_restx import Resource
import requests
from werkzeug.wrappers import Response

BASE_URL = "https://www.imf.org/external/np/fin/data/"


class LastFiveDaysExchangeRate(Resource):
    def get(self):
        endpoint_url = BASE_URL + "rms_five.aspx"
        resp = requests.get(endpoint_url, [("tsvflag", "Y")])
        return Response(resp, status=200)


class MonthlyExchangeRate(Resource):
    def get(self, select_date):
        endpoint_url = BASE_URL + "rms_mth.aspx"
        params = [
            ("SelectDate", f"{select_date}"),
            ("reportType", "SDRCV"),
            ("tsvflag", "Y"),
        ]
        resp = requests.get(endpoint_url, params=params)
        return Response(resp, status=200)
