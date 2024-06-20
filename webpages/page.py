import justpy as jp
from abc import ABC, abstractmethod


class Page(ABC):
    # This is an abstract class representing a web page.

    @abstractmethod
    def serve(self):
        # This method is abstract and must be implemented by subclasses.
        pass

    @classmethod
    def add_footer(cls, parent):
        """Adds a footer to the web page.

        Parameters:
          parent (Element): The parent element to which the footer will be appended.
        """
        # Adds a footer element with copyright information.
        jp.Footer(a=parent, text="© E> - 2024",
                  classes="text-lg text-right text-yellow-400 m-4 fixed-bottom")
