import justpy as jp
from webpages import layout, page


class Home(page.Page):
    path = "/"  # URL path for the home page

    @classmethod
    def serve(cls, request):
        # Create a Quasar page with Tailwind CSS
        wp = jp.QuasarPage(tailwind=True)

        # Use the DefaultLayout for the page
        the_layout = layout.DefaultLayout(a=wp)

        # Create a container for the main content of the page
        container = jp.QPageContainer(a=the_layout)

        # Main div with background color and full height
        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")

        # Add a title to the main content
        jp.Div(a=main_div, text="WordWiz", classes="text-4xl m-2")

        # Add a description to the main content
        jp.Div(a=main_div, text="""
        Welcome to WordWiz, your ultimate destination for instant word definitions. Experience the magic of real-time knowledge as you type, with no need to press any buttons. Our cutting-edge platform is designed to provide you with immediate, accurate definitions to enhance your understanding and expand your vocabulary effortlessly. 
        """, classes="text-lg m-2")

        return wp  # Return the Quasar page
