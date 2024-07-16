from reactpy import component, html

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTStack(
            {"className": "px-10 pb-10"},
            [
                    html.div({"class": "bg-green-100 border  p-5"}, 1),
                    html.div({"class": "bg-green-100 border p-5"}, 2),
                    html.div({"class": "bg-green-100 border p-5"}, 3)
            ]
        ),

        MonacoEditor({
            "defaultValue": """
MTStack(
    [
            html.div(1),
            html.div(2),
            html.div(3)
    ]
)
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True}
        }),

        MTTitle({"order": 3, "className": "pt-5"}, "Usage"),
        html.div(
            {"className": "p-5"},
            "Stack is a vertical flex container. If you need a horizontal flex container, use Group component instead. If you need to have full control over flex container properties, use Flex component."
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
def plot_stack(option):
    return MTProvider(
        build_tab_layout()
    )
