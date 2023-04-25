from gpt_literature_scraper.SearchAPI.Languages import Languages
from serpapi import GoogleScholarSearch


class ScholarSearch:

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, query, language="en", **params):

        # Check if the language code is valid
        if language not in Languages.as_dict():
            raise Exception("Language code not found")

        # TODO: add more parameters
        search = GoogleScholarSearch({
            "q": query, 
            "api_key": self.api_key,
            "hl": language,
            **params,
        })

        # TODO: add error handling
        
        # Get the result as a dictionary
        result = search.get_dict()

        return result