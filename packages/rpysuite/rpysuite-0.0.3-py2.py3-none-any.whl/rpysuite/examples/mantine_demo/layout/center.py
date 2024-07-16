from reactpy import component, html

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex, MTCenter, MTBox
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTCenter(
            {"maw": 400, "h": 100, "bg": "var(--mantine-color-gray-light)",
             "component": 'button', "on_click": lambda x: print('hello')},
            MTBox({"bg": 'var(--mantine-color-gray-light)'}, "All elements inside Center are centered")
        ),

        MonacoEditor({
            "defaultValue": """
MTCenter(
    {"maw": 400, "h": 100, "bg": "var(--mantine-color-gray-light)"},
    MTBox({"bg": 'var(--mantine-color-gray-light)'}, "All elements inside Center are centered")
)
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True}
        }),

        MTTitle({"order": 3, "className": "pt-5"}, "Difference from Group and Stack"),
    )



def build_tab_layout():
    return MTTabs(
        {"defaultValue": "basic", "className": "mx-10"},
        [
            MTTabsList([
                MTTabsTab({"value": "basic"}, "basic"),
                # MTTabsTab({"value": "gutter"}, "gutter"),
            ]),
            MTTabsPanel({"value": "basic"}, basic_panel()),
            # MTTabsPanel({"value": "gutter"}, gutter_panel())
        ]
    )


@component
def plot_center(option):
    return MTProvider(
        build_tab_layout()
    )
