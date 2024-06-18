import justpy as jp


class Home:
    path = "/"  # URL path for the home page

    @classmethod
    def serve(cls, request):
        # Create a Quasar page with Tailwind CSS
        wp = jp.QuasarPage(tailwind=True)

        # Create the layout for the page
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)  # Add a header to the layout
        toolbar = jp.QToolbar(a=header)  # Add a toolbar to the header

        # Create a drawer (sidebar) for the layout
        the_drawer = jp.QDrawer(
            a=layout, show_if_above=True, v_model="leftDrawerOpen", bordered=True)

        # Create a button in the toolbar to toggle the drawer
        toggle_btn = jp.QBtn(a=toolbar, dense=True, flat=True,
                             round=True, icon="menu", click=cls.move_drawer)
        toggle_btn.drawer = the_drawer  # Attach the drawer to the button for easy access

        # Add a title to the toolbar
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        # Create a container for the main content of the page
        container = jp.QPageContainer(a=layout)
        # Main div with background color and full height
        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")

        # Add a title to the main content
        jp.Div(a=main_div, text="This is Home Page", classes="text-4xl m-2")

        # Add a description to the main content
        jp.Div(a=main_div, text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Nulla facilisi. Duis ut eros sit amet justo varius scelerisque non eu erat. Quisque lacinia, metus nec hendrerit pharetra, quam augue venenatis justo, in facilisis odio tortor nec nulla. Morbi euismod, risus et convallis varius, elit est tincidunt ligula, nec scelerisque nisi eros sit amet metus. Aliquam erat volutpat. Proin ut dolor eget erat bibendum facilisis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum in libero euismod, cursus arcu non, dictum urna.
        """, classes="text-lg m-2")

        return wp  # Return the Quasar page

    @staticmethod
    def move_drawer(widget, msg):
        # Toggle the drawer's open/close state
        widget.drawer.value = not widget.drawer.value
