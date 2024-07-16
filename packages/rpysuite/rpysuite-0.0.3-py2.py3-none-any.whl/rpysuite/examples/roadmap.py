from copy import copy

from reactpy import component, html, use_state

from rpysuite.components.mantine import MTProvider, MTCenter, MTText, MTPaper, MTGrid, MTGridCol, MTTitle, MTInputX, \
    MTCode, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTScrollArea, MTNavLink, MTCodeHighlight
from rpysuite.components.markdown import Markdown


@component
def plot_roadmap(option):
    return html.div(
        MTProvider(
            MTPaper(
                {"shadow": 'lg', "class": "mx-10 "},
                Markdown("""
- [x]  add basic examples to the show 
- [x]  support markdown for speeding up the documents
- [x]  upgrade reactpy to github develop version
- [x]  upgrade Mantine to 7.11.1
- [x]  add mantine datatable
- [ ]  add more components
- [ ]  add tutorials
- [ ]  add advanced examples
- [ ]  auth/sso support
- [ ]  pro modules
                """)
            )
        )
    )