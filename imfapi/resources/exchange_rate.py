from flask_restful import Resource
import requests
from werkzeug.wrappers import Response

BASE_URL = "https://www.imf.org/external/np/fin/data/rms_five.aspx"


class ExchangeRate(Resource):
    def get(self):
        resp = requests.get(BASE_URL, [('tsvflag', 'Y')])
        return Response(resp, status=200)
