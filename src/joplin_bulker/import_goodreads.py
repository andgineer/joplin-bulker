import requests
import requests.exceptions
import pandas as pd
from joppy.api import Api, Note


GOODREADS_COLUMN_NAMES = ['Book Id', 'Title', 'Author', 'ISBN', 'My Rating', 'Date Added',
       'Bookshelves', 'My Review']


def get_token() -> str:
    try:
        return requests.post("http://localhost:41184/auth").json()["auth_token"]
    except requests.exceptions.ConnectionError as e:
        print("Please enable Web Clipper service - see in README.md how.")
        exit(1)


def import_good_reads(file_name: str) -> pd.DataFrame:
    books = pd.read_csv(file_name)
    books.dropna(axis=1, how="all", inplace=True)
    books.drop(labels=[
        "Spoiler", "Read Count", "Owned Copies", "Exclusive Shelf",
        'Author l-f', 'Additional Authors',
        'Average Rating', 'Publisher', 'Binding',
        'ISBN13', 'Number of Pages', 'Year Published', 'Original Publication Year',
        'Date Read', 'Bookshelves with positions',
    ], axis=1, inplace=True)
    return books


def create_notes() -> None:
    token = get_token()
    api = Api(token=token)
    item = Note(

    )
    api.add_note(item)


def goodreads_url(id: str) -> str:
    return f"https://www.goodreads.com/book/show/{id}"

def main():
    print(import_good_reads("~/Downloads/goodreads_library_export.csv"))


if __name__ == "__main__":
    main()
