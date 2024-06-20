import logging
import requests
import time
import justpy as jp
from webpages import layout, page
from definition import Definition
from config import DICTIONARY_ROUTE, BASE_URL, WORDWIZ_API_ROUTE, MIN_INPUT_LENGTH


# Retrieve or create logger instance for current module
logger = logging.getLogger(__name__)


class Dictionary(page.Page):
    path = DICTIONARY_ROUTE

    @classmethod
    def serve(cls, request):
        try:
            # Create a QuasarPage instance
            wp = jp.QuasarPage(tailwind=True)

            # Use the DefaultLayout for the page
            the_layout = layout.DefaultLayout(a=wp)

            # Create a container for the main content of the page
            container = jp.QPageContainer(a=the_layout)

            # Main Div for layout with dark background and padding
            main_div = jp.Div(
                a=container, classes="bg-gray-900 min-h-screen p-4")

            # Add a title to the main content with vibrant yellow text
            jp.Div(a=main_div, text="WordWiz: Dive Into Words",
                   classes="text-4xl font-bold text-center text-yellow-400 mb-4")

            # Add a description to the main content with light gray text
            jp.Div(a=main_div, text="Instantly discover the definition of any English word as you type. Enjoy seamless and immediate access to meanings, empowering your understanding and enhancing your vocabulary without any delays.",
                   classes="text-lg text-gray-300 mb-8")

            # Div for input and button (grid layout)
            input_div = jp.Div(
                a=main_div, classes="grid grid-cols-1 md:grid-cols-2 gap-4 items-center justify-center")

            # Div for displaying definitions with vibrant yellow border
            output_div = jp.Div(
                a=main_div, classes="m-2 p-2 text-lg border-2 border-yellow-400 h-60 overflow-auto text-white")

            # Ol (ordered list) component to hold the definitions
            definition_list = jp.Ol(
                a=output_div, classes="list-decimal list-inside m-4")

            # Input box for word entry with larger font size, focus effects, and rounded corners
            input_box = jp.Input(a=input_div, placeholder="Enter your word here", outputdiv=output_div, deflist=definition_list,
                                 classes="m-2 p-2 bg-gray-700 border-2 border-yellow-400 rounded w-full focus:bg-gray-600 focus:outline-none focus:border-yellow-600 text-white text-lg")

            # Event handler for input box to fetch definitions automatically
            input_box.on('input', cls.get_definition)

            cls.add_footer(main_div)  # Add footer to the main content

            return wp  # Return the Quasar page

        except Exception:
            # Log any exceptions using the custom logger
            logger.exception("An exception occurred")

    @staticmethod
    def get_definition(widget, msg):

        # Clear previous definitions
        widget.deflist.delete_components()
        widget.outputdiv.text = ""

        # Get the word from the input box
        word = widget.value.strip()

        if not word:
            # If no word (or deleted) clear output
            widget.outputdiv.text = ""
            return

        # # PREVIOUSLY: Get definitions for the word directly from definition class/app
        # try:
        #     definitions = Definition(word).get()
        # except Exception as e:
        #     # Log the error
        #     logger.error(
        #         f"Error while retrieving definitions for '{word}': {e}")
        #     # Display error message
        #     widget.outputdiv.text = "An error occurred while retrieving definitions. Please try again later."
        #     return

        # Use this app own API to get definitions by sending a GET request to the WordWiz API with a specified timeout (maximum time in seconds that the request should wait for a response from the server before raising exceptions.Timeout exception)
        try:
            if len(word) < MIN_INPUT_LENGTH or not word.isalpha():
                # Minimum input length not met or not letters chars, do not send request to reduce sending too much requests and avoid lagging
                return
            with requests.get(f"{BASE_URL}{WORDWIZ_API_ROUTE}?word={word}", timeout=5) as response:
                response.raise_for_status()
                data = response.json()
                definitions = data['definitions']
        except Exception as e:
            # Log the error
            logger.error(
                f"Error while retrieving definitions for '{word}': {e}")
            # Display error message
            widget.outputdiv.text = "An error occurred while retrieving definitions. Please try again later."
            return

        if not definitions:
            # If definitions list is empty, log then display a message
            widget.outputdiv.text = "No definitions found for this word."
            return

        # Display definitions as list items
        for definition in definitions:
            jp.Li(a=widget.deflist, text=definition,
                  classes="text-lg text-gray-300")
            jp.Br(a=widget.deflist)
