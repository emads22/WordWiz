import logging
import justpy as jp
from webpages import about, dictionary, home, navbar
from config import LOG_FILE


# Create the directory for log files if it doesn't exist, and Ensure parent directories are created if they don't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Configure the logging format and level
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
                    level=logging.DEBUG)


# Define JustPy routes
jp.Route(about.About.path, about.About.serve)
jp.Route(home.Home.path, home.Home.serve)
jp.Route(dictionary.Dictionary.path, dictionary.Dictionary.serve)
jp.Route(navbar.Navbar.path, navbar.Navbar.serve)


if __name__ == "__main__":
    jp.justpy()