from abc import abstractmethod, ABC

from decouple import config


class OneApiRequestProcessor(ABC):
    headers = {
        "Authorization": "Bearer " + config("ONE_API_KEY")
    }

    base_url = config("ONE_API_BASE_URL")

    @abstractmethod
    def process_request(self):
        pass

