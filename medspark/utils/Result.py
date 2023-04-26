import requests
from tika import parser


class SearchResult:
    """
    Result class, with the following attributes:
    result.entry_id: The result's unique identifier
    result.updated: When the result was last updated.
    result.published: When the result was originally published.
    result.title: The title of the result.
    result.authors: The result's authors, as arxiv.Authors.
    result.summary: The result abstract.
    result.comment: The authors' comment if present.
    result.journal_ref: A journal reference if present.
    result.doi: A URL for the resolved DOI to an external resource if present.
    result.primary_category: The result's primary category
    result.categories: All of the result's categories
    result.links: Up to three URLs associated with this result
    result.pdf_url: A URL for the result's PDF if present. Note: this URL also appears among result.links.
    """

    def __init__(
        self,
        entry_id,
        published,
        title,
        authors,
        summary,
        doi,
        primary_category,
        categories,
        links,
        pdf_url,
        text=None,
    ):
        self.entry_id = entry_id
        self.published = published
        self.title = title
        self.authors = authors
        self.summary = summary
        self.doi = doi
        self.primary_category = primary_category
        self.categories = categories
        self.links = links
        self.pdf_url = pdf_url
        self._text = text

    def __str__(self):
        return f"Result: {self.title}"

    def __repr__(self):
        return f"Result: {self.title}"

    def get_text_from_pdf_url(self):
        """
        Returns the text from the PDF URL
        """
        # Fetch the PDF from self.pdf_url
        r = requests.get(self.pdf_url, stream=True)

        # Use tika to read into pdf
        raw = parser.from_buffer(r)

        # Return the text
        return raw["content"].strip()

    @property
    def text(self):
        """
        Returns the text from the PDF URL, calculating it if it has not already been calculated
        """
        if self._text is None:
            self._text = self.get_text_from_pdf_url()
        return self._text

    @staticmethod
    def from_arxiv_result(arxiv_result):
        """
        Creates a SearchResult from an arxiv.Result
        """
        return SearchResult(
            entry_id=arxiv_result.entry_id,
            published=arxiv_result.published,
            title=arxiv_result.title,
            authors=arxiv_result.authors,
            summary=arxiv_result.summary,
            doi=arxiv_result.doi,
            primary_category=arxiv_result.primary_category,
            categories=arxiv_result.categories,
            links=arxiv_result.links,
            pdf_url=arxiv_result.pdf_url,
        )

    @staticmethod
    def from_open_library_result(openlibrary_result):
        
        # Get the PDF URL
        urls = [fmt["url"] for fmt in openlibrary_result["formats"] if fmt["format"] == "PDF"]
        pdf_url = None
        if len(urls) > 0:
            pdf_url = urls[0]

        return SearchResult(
            entry_id=openlibrary_result["id"],
            published=openlibrary_result["copyright_year"],
            title=openlibrary_result["title"],
            authors=openlibrary_result["contributors"],
            summary=openlibrary_result["description"],
            doi=openlibrary_result["ISBN13"],
            primary_category=None,
            categories=openlibrary_result["subjects"],
            links=[openlibrary_result["url"],],
            pdf_url=pdf_url,
        )