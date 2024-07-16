from reactpy import component, html, use_state

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex, MTInputX, MTText, MTTextInput
from rpysuite.components.monaco import MonacoEditor


def basic_panel():

    label, set_label = use_state("The Text shows at here! Click Enter(for InputX component) to update!")
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTText({}, label),
        MTInputX(
            {
                "label": 'Input X',
                "value": label,
                "sync": set_label,
            }
        ),
        MTTextInput(
            {
                "label": 'Text input',
                "value": label,
                "onChange": lambda x: set_label(x.get('target').get('value')),
            }
        ),

        MonacoEditor({
            "defaultValue": """
MTInputX(
    {
        "label": 'Input X',
        "value": label,
        "sync": set_label,
    }
),
MTTextInput(
    {
        "label": 'Text input',
        "value": label,
        "onChange": lambda x: set_label(x.get('target').get('value')),
    }
)
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True},
            "class_name": 'pt-10'
        }),
        MTTitle('Limitations'),
        MTText('Due to limitations of ReactPy, the text input\'s update is a frustrated thing. if you use onChange on the TextInput component. each time you press the key, the focus will be lost.'
               'To avoid this, We make a component that monitoring your inputs, only when you press the enter, it will be updated! (still the focus will be lost)')
    )



def build_tab_layout():
    return MTTabs(
        {"value": 'basic', "className": "mx-10"},
        [
            MTTabsList([
                MTTabsTab({"value": "basic"}, "basic"),
                # MTTabsTab({"value": "controlled"}, "controlled"),
            ]),
            MTTabsPanel({"value": "basic"}, basic_panel()),
            # MTTabsPanel({"value": "controlled"}, controlled_panel())
        ]
    )


@component
def plot_inputx(option):
    return MTProvider(
        build_tab_layout()
    )
