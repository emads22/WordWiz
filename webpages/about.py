import justpy as jp
from webpages import layout, page


class About(page.Page):
    path = "/about"

    def serve(self):
        # Create a QuasarPage instance
        wp = jp.QuasarPage(tailwind=True)

        # Use the DefaultLayout for the page
        the_layout = layout.DefaultLayout(a=wp)

        # Create a container for the main content of the page
        container = jp.QPageContainer(a=the_layout)

        # Main div with background color and full height
        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")

        # Add a title to the main content
        jp.Div(
            a=main_div, text="About Us", classes="text-4xl m-2")

        # Add a description to the main content
        jp.Div(a=main_div, text="""
Welcome to WordWiz, the revolutionary web app designed to redefine how you explore language. At WordWiz, we believe in the power of instant knowledge. Our intuitive platform provides real-time definitions for any word you input, eliminating the need for buttons or delays. Simply type, and watch the meaning unfold before your eyes. Whether you're a student, writer, or language enthusiast, WordWiz is your go-to tool for quick and effortless understanding. Dive into the world of words with unprecedented ease and efficiency, and let WordWiz be your companion in expanding your vocabulary seamlessly.
""", classes="text-lg m-2")

        return wp  # Return the Quasar page
