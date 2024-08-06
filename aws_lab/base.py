import urllib.request
from bs4 import BeautifulSoup


class Base():
    def __init__(self):
        pass

    def page_parse(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }

        soup = []
        for url in self.:
            res = urllib.request.Request(url, headers=header)
            soup.append(BeautifulSoup(res.data, 'html.parser'))

        return soup