from rpysuite.components.icons import Icon

from reactpy import component, html, use_state, use_ref

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex, MTInputX, MTText, MTTextInput, \
    MTButton, MTButtonX, MTTooltip
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    label, set_label = use_state('click 0')

    note, set_note = use_state(None)

    cnt = use_ref(0)

    def click_handler(e):
        cnt.current = cnt.current + 1
        set_label(f'click {cnt.current}')
        set_note(None)

    def click_handlerx(e):
        cnt.current = cnt.current + 1
        set_label(f'click {cnt.current}')
        set_note(f'click {cnt.current}')

    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTText(label),
        MTButton({"w": 100, "onClick": click_handler}, "click me"),
        MTButtonX({ "note": note, "onClick": click_handlerx, "color": 'red',
                    "leftSection": {"name": 'Photo'},
                    "tooltip": {"label": "just to show sth here!"}
                    }, "click me with notes!"),
        MonacoEditor({
            "defaultValue": """

label, set_label = use_state('click 0')

note, set_note = use_state(None)

cnt = use_ref(0)

def click_handler(e):
    cnt.current = cnt.current + 1
    set_label(f'click {cnt.current}')

def click_handlerx(e):
    cnt.current = cnt.current + 1
    set_label(f'click {cnt.current}')
    set_note(f'click {cnt.current}')
    
...
MTText(label),
MTButton({"w": 100, "onClick": click_handler}, "click me"),
MTButtonX({ "note": note, "onClick": click_handlerx, "color": 'red',
            "leftSection": {"name": 'Photo'},
            "tooltip": {"label": "just to show sth here!"}
            }, "click me with notes!"),
...
                """,
            "height": "400px",
            "language": "python",
            "options": {"readOnly": True},
            "class_name": 'pt-10'
        }),
        MTTitle('Limitations'),
        MTText(
            'You can\'t pass params to JS/TS from Python, vise versa.'
            'So the solution to use mantine\'s notification may be a little bit weird, you need to use the use_state from the python side!'
            'You need to keep the note as None when you don\'t need it!'
        )
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
def plot_button(option):
    return MTProvider(
        build_tab_layout()
    )
