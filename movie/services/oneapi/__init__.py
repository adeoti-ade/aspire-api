import request
from abc import abstractmethod, ABC

from decouple import config


class OneApiRequestProcessor(ABC):
    header = {
        "Authorization": config("ONE_API_KEY")
    }

    @abstractmethod
    def process_request(self):
        pass

