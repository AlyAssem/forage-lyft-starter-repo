from abc import ABC, abstractmethod

class Serviceable(ABC):
    """Responible for determining whether an item needs service or not."""
    @abstractmethod
    def needs_service(self):
        pass