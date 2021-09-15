import requests
from oneapi import OneApiRequestProcessor

from utils.exceptions import ServiceUnavailable


class Character(OneApiRequestProcessor):

    def process_request(self):
        url = self.base_url + "/characters"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()

        if str(response.status_code).startswith("5"):
            raise ServiceUnavailable("service is unavailable, try again later")

    def process_characters(self):
        data = self.process_request()
        if data:
            docs = data.get("docs")
        else:
            return

        if docs and isinstance(docs, list):
            return docs
        return

