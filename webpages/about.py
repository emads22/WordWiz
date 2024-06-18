import justpy as jp
from webpages import layout, page


class About(page.Page):
    path = "/about"

    @classmethod
    def serve(cls, request):
        # Create a QuasarPage instance
        wp = jp.QuasarPage(tailwind=True)

        # Use the DefaultLayout for the page
        the_layout = layout.DefaultLayout(a=wp)

        # Create a container for the main content of the page
        container = jp.QPageContainer(a=the_layout)

        # Main div with background color and full height
        main_div = jp.Div(
            a=container, classes="bg-gray-900 text-gray-200 p-4 min-h-screen")

        # Add a title to the main content with matching text color and size
        jp.Div(
            a=main_div, text="About WordWiz", classes="text-4xl font-bold text-yellow-400 text-center mb-4")

        # Add multiple paragraphs for the description
        jp.P(a=main_div, text="WordWiz is your ultimate destination for instant word definitions. Our mission is to empower individuals with the knowledge they need to understand and appreciate language. Whether you're a student, writer, or language enthusiast, WordWiz is here to support you on your journey to expand your vocabulary and deepen your understanding of words.", classes="text-lg text-gray-300 mb-4")

        jp.P(a=main_div, text="We believe in the power of instant knowledge. Our intuitive platform provides real-time definitions for any word you input, eliminating the need for buttons or delays. Simply type, and watch the meaning unfold before your eyes.", classes="text-lg text-gray-300 mb-4")

        jp.P(a=main_div, text="Thank you for choosing WordWiz as your go-to tool for quick and effortless understanding of language. Join us as we dive into the world of words with unprecedented ease and efficiency!", classes="text-lg text-gray-300 mb-4")

        # Add a contact details section
        contact_section = jp.Div(a=main_div, classes="mt-8")
        jp.Div(a=contact_section, text="Contact Us",
               classes="text-2xl font-bold text-yellow-400 mb-2")
        jp.Div(a=contact_section, text="Email: contact@wordwiz.com",
               classes="text-lg text-gray-300 mb-2")
        jp.Div(a=contact_section, text="Phone: +1 (123) 456-7890",
               classes="text-lg text-gray-300 mb-2")
        jp.Div(a=contact_section, text="Address: 123 WordWiz Street, Beirut, Lebanon",
               classes="text-lg text-gray-300")

        cls.add_footer(main_div)  # Add footer to the main content

        return wp  # Return the Quasar page
