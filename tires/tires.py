from abc import ABC, abstractmethod


class Tires(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns whether car tires should be serviced."""
