#!/usr/bin/python3
"""Sends a request to a URL and displays the response body or an error message"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
