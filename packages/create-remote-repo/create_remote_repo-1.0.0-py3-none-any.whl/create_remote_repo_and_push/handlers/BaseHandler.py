from abc import ABC, abstractmethod
from ..models.Repository import Repository


class BaseHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def move_to_next_handler(self, request: Repository):
        if self.next_handler is not None:
            self.next_handler.process(request)
        else:
            return

    @abstractmethod
    def process(self, request: Repository):
        pass
