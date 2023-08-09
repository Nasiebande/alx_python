#!/usr/bin/python3
"""Sends a request to a URL and displays the value of X-Request-Id header"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
