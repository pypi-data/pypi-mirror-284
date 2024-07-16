from reactpy import component, html

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTFlex(
            {"className": "px-10 pb-10", "wrap": 'wrap'},
            [
                html.div({"class": "bg-green-100 border  p-5"}, i) for i in range(100)
            ]
        ),

        MonacoEditor({
            "defaultValue": """
MTFlex(
    {"className": "px-10 pb-10", "wrap": 'wrap'},
    [
        html.div({"class": "bg-green-100 border  p-5"}, i) for i in range(100)
    ]
),
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True}
        }),

        MTTitle({"order": 3, "className": "pt-5"}, "Difference from Group and Stack"),
        html.div(
            {"className": "p-5"},
            "Flex component is an alternative to Group and Stack. Flex is more flexible, it allows creating both horizontal and vertical flexbox layouts, but requires more configuration. Unlike Group and Stack Flex is polymorphic and supports responsive props."
        )
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
def plot_flex(option):
    return MTProvider(
        build_tab_layout()
    )
