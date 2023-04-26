# Interface for search API
class SearchBase:
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, query, language="en", **params):
        raise NotImplementedError

    def get_dict(self, query, language="en", **params):
        raise NotImplementedError

    def get_json(self, query, language="en", **params):
        raise NotImplementedError