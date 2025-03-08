import requests
import pandas as pd
from typing import List, Dict, Optional

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query: str, max_results: int = 100) -> List[Dict]:
    """Fetch papers from PubMed based on a query."""
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(PUBMED_API_URL, params=search_params)
    response.raise_for_status()
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    fetch_response = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    fetch_response.raise_for_status()
    return parse_papers(fetch_response.text)

def parse_papers(xml_data: str) -> List[Dict]:
    """Parse XML data from PubMed to extract paper details."""
    # This is a simplified parser. In practice, you would use an XML parsing library like lxml.
    papers = []
    # Example parsing logic (needs to be implemented fully):
    # Extract title, publication date, authors, affiliations, and emails.
    return papers

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filter papers to include only those with non-academic authors."""
    non_academic_papers = []
    for paper in papers:
        for author in paper.get("authors", []):
            if is_non_academic(author.get("affiliation", "")):
                non_academic_papers.append(paper)
                break
    return non_academic_papers

def is_non_academic(affiliation: str) -> bool:
    """Determine if an affiliation is non-academic."""
    # Heuristic: Check for keywords like 'university', 'college', 'lab', etc.
    academic_keywords = ["university", "college", "lab", "institute"]
    return not any(keyword in affiliation.lower() for keyword in academic_keywords)
