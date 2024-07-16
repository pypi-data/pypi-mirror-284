from copy import copy

from reactpy import component, html, use_state

from rpysuite.components.mantine import MTProvider, MTCenter, MTText, MTPaper, MTGrid, MTGridCol, MTTitle, MTInputX, \
    MTCode, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTScrollArea, MTNavLink, MTCodeHighlight
from rpysuite.components.markdown import Markdown




@component
def plot_about(option):
    return html.div(
        MTProvider(
            MTPaper(
                {"shadow": 'lg', "class": "mx-10 "},
                Markdown("""
Hi, This is dameng!

You can contact me via pingf0@gmail.com . 

Python do save your life!
                """)
            )
        )
    )