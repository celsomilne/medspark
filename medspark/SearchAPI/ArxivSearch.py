import warnings
from medspark.utils import SearchResult, Languages
from medspark.SearchAPI.SearchBase import SearchBase

import arxiv
from arxiv import SortCriterion, SortOrder

# Arxiv search class, extends SearchBase
class ArxivSearch(SearchBase):
    def __init__(self, api_key=None):
        super().__init__(api_key)

    def get(
        self,
        query,
        language="en",
        sort_by=SortCriterion.Relevance,
        sort_order=SortOrder.Descending,
        max_results=10,
        **params
    ):

        # Check if the language code is valid
        if language not in Languages.as_dict():
            raise Exception("Language code not found")

        # Raise a warning that language code is not supported for Arxiv searches, if language is not english
        if language != "en":
            warnings.warn(
                "Language code not supported for Arxiv searches. Defaults to 'en'"
            )

        # Create the arguments
        args = {
            "query": query,
            "max_results": max_results,
            "sort_by": sort_by,
            "sort_order": sort_order,
            **params,
        }

        # Perform the search
        search = arxiv.Search(**args)

        # Return the results
        return [SearchResult.from_arxiv_result(x) for x in search.results()]
