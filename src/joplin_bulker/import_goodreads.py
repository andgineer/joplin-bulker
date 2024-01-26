import sys

import pandas as pd
import requests
import requests.exceptions
from joppy.api import Api

TIMEOUT = 10
GOODREADS_COLUMN_NAMES = [
    "Book Id",
    "Title",
    "Author",
    "ISBN",
    "My Rating",
    "Date Added",
    "Bookshelves",
    "My Review",
]


def get_token() -> str:
    """Get token from Joplin Web Clipper service."""
    try:
        return requests.post("http://localhost:41184/auth", timeout=TIMEOUT).json()["auth_token"]  # type: ignore
    except requests.exceptions.ConnectionError:
        print("Please enable Web Clipper service - see in README.md how.")
        sys.exit(1)


def import_good_reads(file_name: str) -> pd.DataFrame:
    """Import Good Reads CSV file."""
    books = pd.read_csv(file_name)
    books.dropna(axis=1, how="all", inplace=True)
    books.drop(
        labels=[
            "Spoiler",
            "Read Count",
            "Owned Copies",
            "Exclusive Shelf",
            "Author l-f",
            "Additional Authors",
            "Average Rating",
            "Publisher",
            "Binding",
            "ISBN13",
            "Number of Pages",
            "Year Published",
            "Original Publication Year",
            "Date Read",
            "Bookshelves with positions",
        ],
        axis=1,
        inplace=True,
    )
    return books


def create_notes() -> None:
    """Create notes in Joplin."""
    token = get_token()
    Api(token=token)


def goodreads_url(id: str) -> str:
    """Return Good Reads URL."""
    return f"https://www.goodreads.com/book/show/{id}"


def main() -> None:
    """Import."""
    print(import_good_reads("~/Downloads/goodreads_library_export.csv"))


if __name__ == "__main__":
    main()
