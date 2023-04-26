class Result:
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
    def __init__(self, entry_id, updated, published, title, authors, summary, comment, journal_ref, doi, primary_category, categories, links, pdf_url):
        self.entry_id = entry_id
        self.updated = updated
        self.published = published
        self.title = title
        self.authors = authors
        self.summary = summary
        self.comment = comment
        self.journal_ref = journal_ref
        self.doi = doi
        self.primary_category = primary_category
        self.categories = categories
        self.links = links
        self.pdf_url = pdf_url

    def __str__(self):
        return f"Result: {self.title}"

    def __repr__(self):
        return f"Result: {self.title}"

    @staticmethod
    def from_arxiv_result(arxiv_result):
        return Result(
            entry_id=arxiv_result.entry_id,
            updated=arxiv_result.updated,
            published=arxiv_result.published,
            title=arxiv_result.title,
            authors=arxiv_result.authors,
            summary=arxiv_result.summary,
            comment=arxiv_result.comment,
            journal_ref=arxiv_result.journal_ref,
            doi=arxiv_result.doi,
            primary_category=arxiv_result.primary_category,
            categories=arxiv_result.categories,
            links=arxiv_result.links,
            pdf_url=arxiv_result.pdf_url
        )