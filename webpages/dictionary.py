import justpy as jp
from webpages import layout, page
from definition import Definition


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, request):
        # Create a QuasarPage instance
        wp = jp.QuasarPage(tailwind=True)

        # Use the DefaultLayout for the page
        the_layout = layout.DefaultLayout(a=wp)

        # Create a container for the main content of the page
        container = jp.QPageContainer(a=the_layout)

        # Main Div for layout with dark background and padding
        main_div = jp.Div(a=container, classes="bg-gray-900 min-h-screen p-4")

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

        # Input box for word entry with larger font size, focus effects, and rounded corners
        input_box = jp.Input(a=input_div, placeholder="Enter your word here", outputdiv=output_div,
                             classes="m-2 p-2 bg-gray-700 border-2 border-yellow-400 rounded w-full focus:bg-gray-600 focus:outline-none focus:border-yellow-600 text-white text-lg")

        # Event handler for input box to fetch definitions automatically
        input_box.on('input', cls.get_definition)

        cls.add_footer(main_div)  # Add footer to the main content

        return wp  # Return the Quasar page

    @staticmethod
    def get_definition(widget, msg):
        # Get the word from the input box
        word = widget.value
        # Get definitions for the word
        definitions = Definition(word).get()
        # Clear previous content in output div
        widget.outputdiv.text = ""
        # Create an ordered list component to hold the definitions
        definitions_list = jp.Ol(
            a=widget.outputdiv, classes="list-decimal list-inside m-4")
        # Display definitions as list items
        for definition in definitions:
            jp.Li(a=definitions_list, text=definition,
                  classes="text-lg text-gray-300")
            jp.Br(a=definitions_list)
