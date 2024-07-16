from reactpy import component, html

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex, MTContainer
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    demo_props = {
        "bg": 'var(--mantine-color-blue-light)',
        "h": 50,
        "mt": 'md',
    };
    xs_props = {"size": 'xs'}
    xs_props.update(demo_props)
    rem_props = {"size": '30rem', "px": 0}
    rem_props.update(demo_props)
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 "},
        MTContainer(demo_props, "default conatiner"),
        MTContainer(xs_props, "xs conatiner"),
        MTContainer(rem_props, "30rem conatiner without padding"),
        MonacoEditor({
            "defaultValue": """
demo_props = {
    "bg": 'var(--mantine-color-blue-light)',
    "h": 50,
    "mt": 'md',
};
xs_props = {"size": 'xs'}
xs_props.update(demo_props)
rem_props = {"size": '30rem', "px": 0}
rem_props.update(demo_props)
...
(
...
MTContainer(demo_props, "default conatiner"),
MTContainer(xs_props, "xs conatiner"),
MTContainer(rem_props, "30rem conatiner without padding"),
...
)
                """,
            "height": "300px",
            "language": "python",
            "options": {"readOnly": True}
        }),

        MTTitle({"order": 3, "className": "pt-5"}, "Usage"),
        html.div(
            {"className": "p-5"},
            "Container centers content and limits its max-width to the value specified in size prop. Note that the size prop does not make max-width responsive, for example, when it set to lg it will always be lg regardless of screen size."
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
def plot_container(option):
    return MTProvider(
        build_tab_layout()
    )
