from werkzeug.wrappers import Response
from flask import Blueprint
from api.imf.service import get_last_five_days_rate, get_monthwise_rate

BASE_URL = "https://www.imf.org/external/np/fin/data/"

imf_api = Blueprint("imf", __name__, url_prefix="/api/v1/exchangeRate")


@imf_api.get("/lastFiveDays")
def get_last_five_days():
    resp = get_last_five_days_rate()
    return Response(resp, status=200)


@imf_api.get("/monthly/<string:select_date>")
def get_monthly(select_date):
    resp = get_monthwise_rate(select_date)
    return Response(resp, status=200)
