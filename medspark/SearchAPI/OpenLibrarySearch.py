from openlibrary import BookSearch
import requests

from medspark.SearchAPI import SearchBase

from medspark.utils.Result import SearchResult

# OpenLibrary search class
# https://open.umn.edu/opentextbooks/OTL-API.pdf
class OpenLibrarySearch(SearchBase):

    BASE_URI = "https://open.umn.edu/opentextbooks/"
    subjects = [
        "business",
        "accounting",
        "finance",
        "human-resources",
        "management",
        "marketing",
        "computer-science-information-systems",
        "databases",
        "information-systems",
        "programming-languages",
        "education",
        "curriculum-instruction",
        "distance-education",
        "early-childhood",
        "elementary-education",
        "higher-education",
        "secondary-education",
        "engineering",
        "civil",
        "electrical",
        "mechanical",
        "humanities",
        "arts",
        "history",
        "languages",
        "linguistics",
        "literature-rhetoric-and-poetry",
        "music",
        "philosophy",
        "religion",
        "journalism-media-studies-communications",
        "new-media-journalism",
        "law",
        "administrative-law",
        "law-civil-law",
        "constitutional-law",
        "environmental-law",
        "criminal-law",
        "contract-law",
        "property-law",
        "mathematics",
        "algebra",
        "analysis",
        "applied",
        "calculus",
        "geometry-and-trigonometry",
        "pure",
        "statistics",
        "medicine",
        "nursing",
        "nutrition",
        "natural-sciences",
        "biology",
        "chemistry",
        "geology",
        "physics",
        "social-sciences",
        "anthropology",
        "cultural-ethnic-studies",
        "economics",
        "gender-sexuality-studies",
        "geography",
        "political-science",
        "psychology",
        "sociology",
        "student-success",
    ]

    def __init__(self, api_key=None):
        super().__init__(api_key)

    def get(self, query, language="en", page=1, **params):

        subject = query


        # Check that the subject exists
        if subject not in self.subjects:
            raise Exception("Subject not found")

        # Create the URI
        uri = self.BASE_URI + "subjects/" + subject + ".json"

        # Get the results
        resp = requests.get(uri, params={"page": page}).json()["data"]
        
        return [SearchResult.from_open_library_result(x) for x in resp]
