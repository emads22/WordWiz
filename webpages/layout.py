import justpy as jp


class DefaultLayout(jp.QLayout):
    """
    layout was exported from "https://quasar.dev/layout-builder/" and the analogy was made to create html elements
    in the same hierarchy and with same attribues
    """

    def __init__(self, **kwargs):
        # Initialize the base QLayout with provided arguments
        super().__init__(**kwargs)

        # No need anymore for `layout = jp.QLayout(a=wp, view="hHh lpR fFf")` since this is a inherted class from jp.QLayout so the DefaultLayout class instance sends `a` and `view` which they are in kwargs and directly sent to jp.QLayout class using `super()`, then we change all occurences of layout to self and bring back the Event Handler static method from `Home` class and change it from `cls.move_drawer` to `self.move_drawer` cz here its theres an __init__() method

        header = jp.QHeader(a=self)  # Add a header to the layout
        toolbar = jp.QToolbar(a=header)  # Add a toolbar to the header

        # Create a drawer (sidebar) for the layout
        left_drawer = jp.QDrawer(
            a=self, show_if_above=True, v_model="leftDrawerOpen", bordered=True)

        # Add a scroll area to the drawer
        # Scrollable area to hold the list of links
        scroller = jp.QScrollArea(a=left_drawer, classes="fit")

        # Create a list within the scroll area
        qlist = jp.QList(a=scroller)  # List container for navigation links

        # Define the CSS classes for the anchor tags
        a_classes = "m-2 p-2 text-lg text-blue-400 hover:text-blue-700"

        # Add anchor tags (links) to the list
        jp.A(a=qlist, href="/", text="Home", classes=a_classes)  # Home link
        jp.Br(a=qlist)  # Line break for spacing
        jp.A(a=qlist, href="/dictionary", text="Dictionary",
             classes=a_classes)  # Dictionary link
        jp.Br(a=qlist)  # Line break for spacing
        jp.A(a=qlist, href="/about", text="About",
             classes=a_classes)  # About link

        # Create a button in the toolbar to toggle the drawer
        toggle_btn = jp.QBtn(a=toolbar, dense=True, flat=True,
                             round=True, icon="menu", click=self.move_drawer)
        toggle_btn.drawer = left_drawer  # Attach the drawer to the button for easy access

        # Add a title to the toolbar
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        # Toggle the drawer's open/close state
        widget.drawer.value = not widget.drawer.value
