# Aganitha-Task

Initialize the Project with Poetry:

poetry new get_papers_list
cd get_papers_list
Add Dependencies:

poetry add requests pandas
Create the Project Structure:

get_papers_list/
├── get_papers_list/
│   ├── __init__.py
│   ├── cli.py
│   ├── fetcher.py
│   └── utils.py
├── tests/
│   └── __init__.py
├── pyproject.toml
└── README.md

# Get Papers List

This project fetches research papers from PubMed based on a user-specified query and filters papers with at least one author affiliated with a pharmaceutical or biotech company.

## Installation

1. Install Poetry if you haven't already:
   ```bash
   pip install poetry

2.Clone the repository and install dependencies:

git clone https://github.com/yourusername/get_papers_list.git
cd get_papers_list
poetry install

To fetch papers and save the results to a CSV file:
poetry run get-papers-list "your query here" -f output.csv

To print the results to the console:
poetry run get-papers-list "your query here"

Dependencies
requests: For making HTTP requests to the PubMed API.

pandas: For handling data and generating CSV files.

Tools Used
Poetry: For dependency management and packaging.

PubMed API: For fetching research papers.

Publish the Module to Test PyPI (Bonus)

1. **Build the Package:**
   ```bash
   poetry build
Publish to Test PyPI:

poetry publish -r test-pypi
Test the Program
Run the program with different queries and options to ensure it works as expected.
poetry run get-papers-list "cancer treatment" -f output.csv
