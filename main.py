import inspect
import justpy as jp
from webpages.home import Home
from webpages.about import About
from webpages.dictionary import Dictionary
from webpages.wordwiz_api_docs import WordWizAPIDocs
from webpages.page import Page
from app_logger import AppLogger


# Initialize an AppLogger instance
app_logger = AppLogger().logger

# The globals() dictionary can change dynamically as new variables and functions are defined. Looping through globals().items() directly can cause errors if the dictionary is modified during iteration. Converting it to a list first prevents this issue by creating a static snapshot of the current global objects.
imports = list(globals().values())

# Iterate through each object in the list of global objects
for obj in imports:
    # # METHOD 1:
    # # Check if the object has both 'path' and 'serve' attributes
    # if hasattr(obj, 'path') and hasattr(obj, 'serve'):
    #     # Register the route with JustPy
    #     jp.Route(obj.path, obj.serve)

    # METHOD 2: more robust using abstract class
    # Check if the object is a class
    if inspect.isclass(obj):
        # Check if the class is a subclass of the abstract class 'Page' and not the 'Page' class itself
        if issubclass(obj, Page) and obj is not Page:
            # Register the route with JustPy
            jp.Route(obj.path, obj.serve)

if __name__ == "__main__":

    try:
        jp.justpy()

    except Exception:
        # Log the exception with stack trace (automatically without passing {e} cz `logger.exception()`)
        app_logger.exception("An unexpected error occurred")
