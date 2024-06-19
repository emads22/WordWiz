import logging
import inspect
import justpy as jp
from webpages.home import Home
from webpages.about import About
from webpages.dictionary import Dictionary
from webpages.documentation import Documentation
from webpages.page import Page
from config import LOG_FILE


# Create the directory for log files if it doesn't exist, and Ensure parent directories are created if they don't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


# # Configure the logging format and level
# logging.basicConfig(filename=LOG_FILE,
#                     format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
#                     level=logging.DEBUG)


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
    jp.justpy()
