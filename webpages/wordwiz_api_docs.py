import logging
import justpy as jp
from webpages import layout, page
from config import API_DOCS_ROUTE


# Retrieve or create logger instance for current module
logger = logging.getLogger(__name__)


class WordWizAPIDocs(page.Page):
    path = API_DOCS_ROUTE

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
            jp.Div(a=main_div, text="WordWiz API Documentation",
                   classes="text-4xl font-bold text-center mb-8")

            # Add usage instructions
            jp.Div(a=main_div, text="Usage", classes="text-2xl font-bold mb-4")
            jp.Div(a=main_div, text="To use this API, you can make GET requests to the following endpoint:",
                   classes="text-lg text-gray-300 mb-2")
            jp.Div(a=main_div, text="/wordwiz-api/v1/define?word=<word>",
                   classes="text-lg mb-2")
            jp.Div(a=main_div, text="Replace <word> with the word you want to define.",
                   classes="text-lg text-gray-300 mb-4")

            # Add example request
            jp.Div(a=main_div, text="Example Request",
                   classes="text-2xl font-bold mt-8 mb-4")
            jp.A(a=main_div,
                 href="http://127.0.0.1:8080/wordwiz-api/v1/define?word=car",
                 text="http://127.0.0.1:8080/wordwiz-api/v1/define?word=car",
                 classes="text-lg text-gray-300 mb-2 underline hover:text-yellow-400",
                 target="_blank")

            # Add response format
            jp.Div(a=main_div, text="Response Format",
                   classes="text-2xl font-bold mt-8 mb-4")
            jp.Div(a=main_div, text="The API returns JSON data with the following format:",
                   classes="text-lg text-gray-300 mb-2")

            jp.parse_html(a=main_div, html_string="""
<pre class="text-lg mb-4">
{
  "word": "car",
  "definitions": [
    "A four-wheeled motor vehicle used for land transport."
  ]
}
</pre>
""")

            cls.add_footer(main_div)  # Add footer to the main content

            return wp  # Return the Quasar page

        except Exception:
            # Log any exceptions using the custom logger
            logger.exception("An exception occurred")
