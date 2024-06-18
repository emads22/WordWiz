from abc import ABC, abstractmethod

class Page(ABC):
    # This is an abstract class representing a web page.

    @abstractmethod
    def serve(self):
        # This method is abstract and must be implemented by subclasses.
        pass
