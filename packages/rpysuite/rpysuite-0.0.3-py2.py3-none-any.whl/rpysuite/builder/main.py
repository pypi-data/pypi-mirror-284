from fastapi import FastAPI

from reactpy import component, html
from reactpy.backend._common import CommonOptions
from reactpy.backend.fastapi import configure
from rpysuite.builder.loader import load_mantine, load_component

app = FastAPI()

data = {
    "component": 'MTProvider',
    'props': {},
    "children": [{
    'component': 'MTGrid',
    'props': {},
    'children': [

        {
            'component': 'MTGridCol',
            'props': {"span": 5},
            'children': [
                {
                    'component': 'MTText',
                    'props': {},
                    'children': ["123"]
                },
            ]
        },
        {
            'component': 'MTGridCol',
            'props': {"span": 5, },
            'children': [
                {
                    'component': 'MTText',
                    'props': {"color": 'red'},
                    'children': ["456"]
                },
            ]
        },
        {
            'component': 'MTGridCol',
            'props': {"span": 2},
            'children': [
                {
                    'component': 'MTText',
                    'props': {},
                    'children': [
                        {
                            'component': 'h1',
                            'props': {
                                "style": {
                                    "color": 'blue'
                                }
                            },
                            'children': [
                                "789"
                            ]
                        },
                    ]
                },
            ]
        },
    ]
}]

}

def traverse(node):
    if isinstance(node, str) or isinstance(node, int) or isinstance(node, float):
        return node
    component_name = node.get('component')
    component_props = node.get('props')
    component_children = node.get('children')
    rendered = load_component(component_name)(component_props or {}, [traverse(child) for child in component_children])
    return rendered


@component
def render():
    return traverse(data)



options = CommonOptions(head=[html.title('Demo')])
options.cors = False
configure(app, render, options=options)