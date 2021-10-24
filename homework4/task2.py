"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
count_dots_on_i("https://example.com/")
59
* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import logging

import requests
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError


def count_dots_on_i(url: str) -> int:
    """count how many letters `i` are present in the HTML by this URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.count("i")
    except (ConnectTimeout, ConnectionError):
        raise ValueError(f"Unreachable {url}")
    except HTTPError:
        logging.error(f"status_code: {response.status_code}, body: {response.content}")  # type: ignore
    return 0


if __name__ == "__main__":  # pragma: no cover
    print(count_dots_on_i("https://examp.com"))
