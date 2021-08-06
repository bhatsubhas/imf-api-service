import requests
BASE_URL = "https://www.imf.org/external/np/fin/data/"


def get_last_five_days_rate():
    endpoint_url = BASE_URL + "rms_five.aspx"
    resp = requests.get(endpoint_url, [("tsvflag", "Y")])
    return resp


def get_monthwise_rate(select_date):
    endpoint_url = BASE_URL + "rms_mth.aspx"
    params = [
        ("SelectDate", f"{select_date}"),
        ("reportType", "SDRCV"),
        ("tsvflag", "Y"),
    ]
    resp = requests.get(endpoint_url, params=params)
    return resp
