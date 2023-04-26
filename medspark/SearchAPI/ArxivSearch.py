from medspark.SearchAPI.SearchBase import SearchBase

# Arxiv search class, extends SearchBase
class ArxivSearch(SearchBase):
    def __init__(self, api_key):
        super().__init__(api_key)

    def get(self, query, language="en", **params):
        # Check if the language code is valid
        if language not in Languages.as_dict():
            raise Exception("Language code not found")