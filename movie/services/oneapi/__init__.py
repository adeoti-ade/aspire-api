import request
from abc import abstractmethod, ABC

from decouple import config


class OneApiRequestProcessor(ABC):
    header = {
        "Authorization": config("ONE_API_KEY")
    }

    base_url = config("ONE_API_BASE_URL")

    @abstractmethod
    def process_request(self):
        pass

