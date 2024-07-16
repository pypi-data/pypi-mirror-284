from reactpy import component, html

from rpysuite.components.mantine import MTGrid, MTGridCol, MTProvider, MTPaper, \
    MTTitle, MTSelect, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTStack, MTFlex, MTCenter, MTBox, MTDataTable, MTText
from rpysuite.components.monaco import MonacoEditor
from rpysuite.examples.mantine_demo.datatable.data import companies

def row_color(row, idx):
    return 'red'

def basic_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        [

            MTDataTable({
                "columns":[{"accessor": "name"}, {"accessor": "streetAddress"}, {"accessor": "city"}, {"accessor": "state"}],
                "records": companies,
            }),

            MonacoEditor({
                "defaultValue": """
MTDataTable({
    "columns":[{"accessor": "name"}, {"accessor": "streetAddress"}, {"accessor": "city"}, {"accessor": "state"}],
    "records": companies,
})
                """,
                "height": "200px",
                "language": "python",
                "options": {"readOnly": True}
            }),

            MTTitle({"order": 3, "className": "pt-5"}, "Data Tables!"),
        ]
    )

def color_panel():
    return MTPaper(
        {"shadow": 'lg', "className": "m-10 p-10"},
        [

        MTDataTable({
            "columns":[{"accessor": "name"}, {"accessor": "streetAddress"}, {"accessor": "city"}, {"accessor": "state"}],
            "records": companies,
            "withTableBorder":True,
            "withColumnBorders": True,
            "rowColorMap": {'state': [{"field": 'MA', "color": 'violet'}]},
            "rowBackgroundColorMap": {'state': [{"field": 'WY', "color": 'red'}]},
            "c": {"dark": '#dbc7a0', "light": '#55350d'},
            "backgroundColor": { "dark": '#232b25', "light": '#f0f7f1' },
        }),

        MonacoEditor({
            "defaultValue": """
MTDataTable({
    "columns":[{"accessor": "name"}, {"accessor": "streetAddress"}, {"accessor": "city"}, {"accessor": "state"}],
    "records": companies,
    "withTableBorder":True,
    "withColumnBorders": True,
    "rowColorMap": {'state': [{"field": 'MA', "color": 'violet'}]},
    "rowBackgroundColorMap": {'state': [{"field": 'WY', "color": 'red'}]},
    "c": {"dark": '#dbc7a0', "light": '#55350d'},
    "backgroundColor": { "dark": '#232b25', "light": '#f0f7f1' },
})
                """,
            "height": "200px",
            "language": "python",
            "options": {"readOnly": True}
        }),

        MTTitle({"order": 3, "className": "pt-5"}, "Limitations"),
            MTText("rowColor & rowBackgroundColor does not work as passing data from py to ts seems not work here, so use the rowColorMap & rowBackgroundColorMap instead!")
        ]
    )



def build_tab_layout():
    return MTTabs(
        {"defaultValue": "basic", "className": "mx-10"},
        [
            MTTabsList([
                MTTabsTab({"value": "basic"}, "basic"),
                MTTabsTab({"value": "color"}, "color"),
                # MTTabsTab({"value": "gutter"}, "gutter"),
            ]),
            MTTabsPanel({"value": "basic"}, basic_panel()),
            MTTabsPanel({"value": "color"}, color_panel()),
            # MTTabsPanel({"value": "gutter"}, gutter_panel())
        ]
    )


@component
def plot_datatable(option):
    return MTProvider(
        build_tab_layout()
    )
