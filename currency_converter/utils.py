import requests

from urllib.parse import urlencode
from currency_converter.config import OXR_API_ID


def call_oxr_api(endpoint, path_params={}, query_params={}):
    query_params.update({'app_id': OXR_API_ID})
    result = requests.get('https://openexchangerates.org/api/%s/%s?%s' %
                          (endpoint, '/'.join([str(x) for x in path_params]),
                           urlencode(query_params))).json()
    if 'error' in result:
        raise Exception
    else:
        return result
