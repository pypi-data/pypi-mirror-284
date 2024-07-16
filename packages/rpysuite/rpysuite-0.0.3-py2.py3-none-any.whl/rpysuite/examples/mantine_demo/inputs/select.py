from reactpy import component, html, use_state

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex
from rpysuite.components.monaco import MonacoEditor


def basic_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        MTSelect(
            {"className": "px-10 pb-10",
             "label": 'your favorite frontend library',
             "placeholder": 'Pick value',
             "data": ['React', 'Angular', 'Vue', 'Svelte']
             }
        ),

        MonacoEditor({
            "defaultValue": """
MTSelect(
    {"className": "px-10 pb-10",
     "label": 'your favorite frontend library',
     "placeholder": 'Pick value',
     "data": ['React', 'Angular', 'Vue', 'Svelte']
     }
)
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True}
        })
    )


def controlled_panel():
    selected, set_selected = use_state({"value": "react", "label":"React"})
    def on_change(v, option):
        set_selected(option)

    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        [

            MTTitle({"order": 2, "className": 'px-10'}, selected.get('value')),
            MTSelect(
                {
                     "className": "px-10 pb-10",
                     "label": 'your favorite frontend library',
                     "placeholder": 'Pick value',
                     "data": [
                            {"value": 'React', "label": 'react'},
                            {"value": 'Angular', "label": 'angular'},
                            {"value": 'VUE', "label": 'vue'},
                            {"value": 'Svelte', "label": 'svelte'},
                     ],
                     "value": selected.get('value') ,
                     "onChange": on_change
                 }
            ),

            MonacoEditor({
                "defaultValue": """
selected, set_selected = use_state({"value": "react", "label":"React"})

def on_change(v, option):
    set_selected(option)
    
...    
MTSelect(
    {
         "className": "px-10 pb-10",
         "label": 'your favorite frontend library',
         "placeholder": 'Pick value',
         "data": [
                {"value": 'React', "label": 'react'},
                {"value": 'Angular', "label": 'angular'},
                {"value": 'VUE', "label": 'vue'},
                {"value": 'Svelte', "label": 'svelte'},
         ],
         "value": selected.get('value') ,
         "onChange": on_change
     }
)
...
                """,
                "height": "300px",
                "language": "python",
                "options": {"readOnly": True}
            }),


        ]
    )

def build_tab_layout():
    selected, set_selected = use_state('basic')
    def on_change(option):
        print(option)
        set_selected(option)
    return MTTabs(
        {"value": selected, "on_change": on_change, "className": "mx-10"},
        [
            MTTabsList([
                MTTabsTab({"value": "basic"}, "basic"),
                MTTabsTab({"value": "controlled"}, "controlled"),
            ]),
            MTTabsPanel({"value": "basic"}, basic_panel()),
            MTTabsPanel({"value": "controlled"}, controlled_panel())
        ]
    )


@component
def plot_select(option):
    return MTProvider(
        build_tab_layout()
    )
