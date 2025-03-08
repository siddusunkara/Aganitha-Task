import argparse
import sys
from typing import Optional
from .fetcher import fetch_papers, filter_non_academic_authors
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed query string.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save the results.")
    args = parser.parse_args()

    try:
        papers = fetch_papers(args.query)
        filtered_papers = filter_non_academic_authors(papers)
        df = pd.DataFrame(filtered_papers)
        
        if args.file:
            df.to_csv(args.file, index=False)
            print(f"Results saved to {args.file}")
        else:
            print(df.to_string(index=False))
    except Exception as e:
        if args.debug:
            print(f"Error: {e}", file=sys.stderr)
        else:
            print("An error occurred. Use --debug for more information.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
