from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns whether a car engine should be serviced when returned to service."""
