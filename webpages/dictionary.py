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

        # Main Div for layout
        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")

        # Add a title to the main content
        jp.Div(a=main_div, text="WordWiz Dictionary",
               classes="text-4xl m-2")

        # Add a description to the main content
        jp.Div(a=main_div, text="Instantly discover the definition of any English word as you type. Enjoy seamless and immediate access to meanings, empowering your understanding and enhancing your vocabulary without any delays.",
               classes="text-lg m-2")

        # Div for input and button (grid layout)
        input_div = jp.Div(a=main_div, classes="grid grid-cols-2")

        # Div for displaying definitions
        output_div = jp.Div(
            a=main_div, classes="m-2 p-2 text-lg border-2 border-gray-300 h-40")

        # Input box for word entry
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4 ")

        # # METHOD 1: Event handler for input box to fetch definitions using a button
        # jp.Button(a=input_div, text="Define", classes="border-2 text-gray-500",
        #           inputbox=input_box, outputdiv=output_div).on('click', cls.get_definition)

        # METHOD 2: Event handler for input box to fetch definitions automatically
        input_box.on('input', cls.get_definition_auto)

        return wp  # Return the Quasar page

    @staticmethod
    def get_definition(widget, msg):
        # Get the word from the input box
        word = widget.inputbox.value
        # Get definitions for the word
        definitions = Definition(word).get()
        # Display definitions in the output div
        widget.outputdiv.text = " --- ".join(definitions)

    @staticmethod
    def get_definition_auto(widget, msg):
        # Get the word from the input box
        word = widget.value
        # Get definitions for the word
        definitions = Definition(word).get()
        # Display definitions in the output div
        widget.outputdiv.text = " --- ".join(definitions)
