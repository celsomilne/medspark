# Interface for search API
import requests

class SearchBase:

    BASE_URI = None

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, query, language="en", **params):
        raise NotImplementedError

    def get_dict(self, query, language="en", **params):
        raise NotImplementedError

    def get_uri(self, **kwargs):
        resp = requests.get(self.BASE_URI, params=kwargs)
        return resp.json()
