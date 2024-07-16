from rpysuite.examples.about import plot_about
from rpysuite.examples.echarts_demo.basic_demo import plot_echarts_line
from rpysuite.examples.home import plot_home
from rpysuite.examples.mantine_demo.datatable.table import plot_datatable
from rpysuite.examples.mantine_demo.inputs.button import plot_button
from rpysuite.examples.mantine_demo.inputs.checkbox import plot_checkbox
from rpysuite.examples.mantine_demo.inputs.select import plot_select
from rpysuite.examples.mantine_demo.inputs.inputx import plot_inputx
from rpysuite.examples.mantine_demo.layout.center import plot_center
from rpysuite.examples.mantine_demo.layout.container import plot_container
from rpysuite.examples.mantine_demo.layout.flex import plot_flex
from rpysuite.examples.mantine_demo.layout.grid import plot_grid
from rpysuite.examples.mantine_demo.layout.stack import plot_stack
from rpysuite.examples.roadmap import plot_roadmap

menu = [
    {"key": "HOME", "name": "Home",  "path": "/" },
    {
        "key": "MANTINE", "name": "Mantine", "path": "/mantine",
        "subs": [
            {
                "key": "LAYOUT", "name": "Layout", "path": "/layout",
                "subs": [
                    {
                        "key": "GRID", "name": "Grid", "option": {"mode": "basic"},
                        "path": "/grid",
                    },
                    {
                        "key": "STACK", "name": "Stack", "option": {"mode": "basic"},
                        "path": "/stack",
                    },
                    {
                        "key": "FLEX", "name": "Flex", "option": {"mode": "basic"},
                        "path": "/flex",
                    },
                    {
                        "key": "CONTAINER", "name": "Container", "option": {"mode": "basic"},
                        "path": "/container",
                    },
                    {
                        "key": "CENTER", "name": "Center", "option": {"mode": "basic"},
                        "path": "/center",
                    },
                ]
            },

            {
                "key": "INPUTS", "name": "Inputs", "path": "/inputs", "icon": "LayoutBoard",
                "subs": [
                    {
                        "key": "CHECKBOX", "name": "Checkbox", "option": {"mode": "basic"},
                        "path": "/checkbox",
                    },
                    {
                        "key": "SELECT", "name": "Select", "option": {"mode": "basic"},
                        "path": "/select",
                    },
                    {
                        "key": "INPUTX", "name": "InputX", "option": {"mode": "basic"},
                        "path": "/inputx",
                    },
                    {
                        "key": "BUTTONX", "name": "ButtonX", "option": {"mode": "basic"},
                        "path": "/buttonx",
                    },
                ]
            },
        ]
    },
    {"key": "DATATABLE", "name": "DataTable", "path": "/datatable",

     "subs": [
         {
             "key": "BASIC", "name": "Basic", "path": "/basic",
         },


     ]
     },
    {"key": "ECHARTS", "name": "ECharts", "path": "/echarts",

     "subs": [
         {
             "key": "BASIC", "name": "Basic", "path": "/basic",
          },


     ]
     },

    {
        "key": "ROADMAP", "name": "Roadmap", "option": None,
        "path": "/roadmap",
    },
    {
        "key": "ABOUT", "name": "About", "option": None,
        "path": "/about",
    },
]



views = {
    "HOME": {"fun": plot_home, "opt": None},
    "MANTINE_LAYOUT_GRID": {"fun": plot_grid, "opt": None},
    "MANTINE_LAYOUT_STACK": {"fun": plot_stack, "opt": None},
    "MANTINE_LAYOUT_FLEX": {"fun": plot_flex, "opt": None},
    "MANTINE_LAYOUT_CENTER": {"fun": plot_center, "opt": None},
    "MANTINE_LAYOUT_CONTAINER": {"fun": plot_container, "opt": None},
    "MANTINE_INPUTS_CHECKBOX": {"fun": plot_checkbox, "opt": None},
    "MANTINE_INPUTS_SELECT": {"fun": plot_select, "opt": None},
    "MANTINE_INPUTS_INPUTX": {"fun": plot_inputx, "opt": None},
    "MANTINE_INPUTS_BUTTONX": {"fun": plot_button, "opt": None},
    "DATATABLE_BASIC": {"fun": plot_datatable, "opt": None},
    "ECHARTS_BASIC": {"fun": plot_echarts_line, "opt": None},
    "ROADMAP": {"fun": plot_roadmap, "opt": None},
    "ABOUT": {"fun": plot_about, "opt": None},
}

icons = {
    "MANTINE_LAYOUT": "LayoutBoard",
    "MANTINE_INPUTS": "KeyboardShow",
    "ECHARTS": "ChartHistogram",
    "MANTINE_LAYOUT_GRID": {"name": "LayoutBoard", "color": "green", "size": 16},
    "MANTINE_LAYOUT_STACK": {"name": "LayoutBoard", "color": "green", "size": 16},
    "MANTINE_LAYOUT_FLEX": {"name": "LayoutBoard", "color": "green", "size": 16},
    "MANTINE_LAYOUT_CONTAINER": {"name": "LayoutBoard", "color": "green", "size": 16},
    "MANTINE_LAYOUT_CENTER": {"name": "LayoutBoard", "color": "green", "size": 16},
    "MANTINE_INPUTS_CHECKBOX": {"name": "Checkbox", "color": "green", "size": 16},
    "MANTINE_INPUTS_SELECT": {"name": "Select", "color": "green", "size": 16},
    "MANTINE_INPUTS_INPUTX": {"name": "InputCheck", "color": "green", "size": 16},
    "MANTINE_INPUTS_BUTTONX": {"name": "Click", "color": "green", "size": 16},
    "DATATABLE_BASIC": {"name": "ChartHistogram", "color": "green", "size": 16},
    "ECHARTS_BASIC": {"name": "ChartHistogram", "color": "green", "size": 16},
    "ROADMAP": {"name": "ChartHistogram", "color": "green", "size": 16},
    "ABOUT": {"name": "ChartHistogram", "color": "green", "size": 16},
}
