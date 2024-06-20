import logging
import justpy as jp
from config import HOME_ROUTE, DICTIONARY_ROUTE, ABOUT_ROUTE, API_DOCS_ROUTE


# Retrieve or create logger instance for current module
logger = logging.getLogger(__name__)


class DefaultLayout(jp.QLayout):
    """
    Layout was exported from "https://quasar.dev/layout-builder/" and the analogy was made to create html elements
    in the same hierarchy and with same attributes.
    """

    def __init__(self, view="hHh lpR fFf", **kwargs):
        # No need anymore for `layout = jp.QLayout(a=wp, view="hHh lpR fFf")` since this is a inherted class from jp.QLayout so the DefaultLayout class instance sends `a` and `view` which they are in kwargs and directly sent to jp.QLayout class using `super()`, then we change all occurences of layout to self and bring back the Event Handler static method from `Home` class and change it from `cls.move_drawer` to `self.move_drawer` cz here its theres an __init__() method

        # Initialize the base QLayout with provided arguments
        super().__init__(view=view, **kwargs)

        try:
            # Add a header to the layout with a dark background and yellow text
            header = jp.QHeader(a=self, classes="bg-gray-800 text-yellow-400")

            # Add a toolbar to the header with matching background
            toolbar = jp.QToolbar(a=header, classes="bg-gray-800")

            # Create a drawer (sidebar) for the layout with a dark background and light text
            left_drawer = jp.QDrawer(
                a=self, show_if_above=True, v_model="leftDrawerOpen", bordered=True, classes="bg-gray-900 text-gray-300")

            # Add a scroll area to the drawer with a dark background
            scroller = jp.QScrollArea(a=left_drawer, classes="fit bg-gray-900")

            # Create a list within the scroll area
            qlist = jp.QList(a=scroller, classes="bg-gray-900 mt-6")

            # Define the CSS classes for the anchor tags to use the color scheme
            a_classes = "m-3 p-2 text-lg text-yellow-400 hover:text-yellow-600"

            # Add anchor tags (links) to the list
            jp.A(a=qlist, href=HOME_ROUTE, text="Home",
                 classes=a_classes)  # Home link
            jp.Br(a=qlist)  # Line break for spacing
            jp.A(a=qlist, href=DICTIONARY_ROUTE, text="Dictionary",
                 classes=a_classes)  # Dictionary link
            jp.Br(a=qlist)  # Line break for spacing
            jp.A(a=qlist, href=ABOUT_ROUTE, text="About",
                 classes=a_classes)  # About link
            jp.Br(a=qlist)  # Line break for spacing
            jp.A(a=qlist, href=API_DOCS_ROUTE, text="API Documentation",
                 classes=a_classes)  # About link

            # Create a button in the toolbar to toggle the drawer, styled with yellow text
            toggle_btn = jp.QBtn(a=toolbar, dense=True, flat=True,
                                 round=True, icon="menu", click=self.move_drawer, classes="text-yellow-400")
            toggle_btn.drawer = left_drawer  # Attach the drawer to the button for easy access

            # Add a title to the toolbar with yellow text
            jp.QToolbarTitle(a=toolbar, text="WordWiz",
                             classes="text-yellow-400")

        except Exception:
            # Log any exceptions using the custom logger
            logger.exception("An exception occurred")

    @staticmethod
    def move_drawer(widget, msg):
        # Toggle the drawer's open/close state
        widget.drawer.value = not widget.drawer.value
