import logging
import justpy as jp
from webpages import layout, page
from config import HOME_ROUTE


# Retrieve or create logger instance for current module
logger = logging.getLogger(__name__)


class Home(page.Page):
    path = HOME_ROUTE

    @classmethod
    def serve(cls, request):
        try:
            # Create a Quasar page with Tailwind CSS
            wp = jp.QuasarPage(tailwind=True)

            # Use the DefaultLayout for the page
            the_layout = layout.DefaultLayout(a=wp)

            # Create a container for the main content of the page
            container = jp.QPageContainer(a=the_layout)

            # Main div with dark background color and full height
            main_div = jp.Div(
                a=container, classes="bg-gray-900 text-yellow-300 min-h-screen p-4")

            # Add a title to the main content with large font size and bold text
            jp.Div(a=main_div, text="WordWiz",
                   classes="text-5xl font-bold text-center mb-8")

            # Add a description to the main content with lighter text color
            jp.Div(a=main_div, text="""
            Welcome to WordWiz, your ultimate destination for instant word definitions. Experience the magic of real-time knowledge as you type, with no need to press any buttons. Our cutting-edge platform is designed to provide you with immediate, accurate definitions to enhance your understanding and expand your vocabulary effortlessly. 
            """, classes="text-lg text-gray-300 leading-relaxed")

            cls.add_footer(main_div)  # Add footer to the main content

            return wp  # Return the Quasar page

        except Exception:
            # Log any exceptions using the custom logger
            logger.exception("An exception occurred")
