from abc import ABC, abstractmethod


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns whether a battery should be serviced when returned to service."""
