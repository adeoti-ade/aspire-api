import requests
from movie.services.oneapi import OneApiRequestProcessor
from movie.models import Character

from utils.exceptions import ServiceUnavailable


class QuotesProcessor(OneApiRequestProcessor):
    query = {
        "limit": 10000
    }

    def process_request(self):
        url = self.base_url + "/quote"
        response = requests.get(url, headers=self.headers, params=self.query)
        if response.status_code == 200:
            return response.json()

        if str(response.status_code).startswith("5"):
            raise ServiceUnavailable("service is unavailable, try again later")

    def process_quotes(self):
        data = self.process_request()
        if data:
            docs = data.get("docs")
        else:
            return

        if docs and isinstance(docs, list):
            return docs
        return

