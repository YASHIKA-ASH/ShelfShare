import requests


def search_google_books(title: str, author: str):

    query = f"{title} {author}"

    url = "https://www.googleapis.com/books/v1/volumes"

    response = requests.get(
        url,
        params={
            "q": query
        }
    )

    data = response.json()

    return data