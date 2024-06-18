import justpy as jp
from webpages import layout


class About:
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
            a=main_div, text="This is About Page", classes="text-4xl m-2")

        # Add a description to the main content
        jp.Div(a=main_div, text="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Nulla facilisi. Duis ut eros sit amet justo varius scelerisque non eu erat. Quisque lacinia, metus nec hendrerit pharetra, quam augue venenatis justo, in facilisis odio tortor nec nulla. Morbi euismod, risus et convallis varius, elit est tincidunt ligula, nec scelerisque nisi eros sit amet metus. Aliquam erat volutpat. Proin ut dolor eget erat bibendum facilisis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum in libero euismod, cursus arcu non, dictum urna.
""", classes="text-lg m-2")

        return wp  # Return the Quasar page
