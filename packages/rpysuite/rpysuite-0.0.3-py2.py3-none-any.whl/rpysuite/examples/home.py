from copy import copy

from reactpy import component, html, use_state

from rpysuite.components.mantine import MTProvider, MTCenter, MTText, MTPaper, MTGrid, MTGridCol, MTTitle, MTInputX, \
    MTCode, MTTabs, MTTabsList, MTTabsTab, MTTabsPanel, MTScrollArea, MTNavLink, MTCodeHighlight
from rpysuite.components.markdown import Markdown


def render_real_todo():
    todos, set_todos = use_state([])
    def add_todo(e):
        todos.insert(0, {"done": False, "value": e})
        set_todos(copy(todos))
    def done_todo(i):
        def wrap(e):
            todos[i]["done"] = not todos[i]["done"]
            set_todos(copy(todos))
        return wrap
    def del_todo(i):
        def wrap(e):
            todos and todos.pop(i) and set_todos(copy(todos))
        return wrap

    return html.div(
        [
            MTInputX({
                "sync": add_todo,
                "style": { "width": 400 }
            }),
            html.ul(
                [html.li({
                    "on_click": done_todo(i),
                    "on_double_click": del_todo(i),
                    "style": {"text-decoration": v.get('done') and 'line-through'}
                }, v.get('value')) for i,v in enumerate(todos)]
            )
        ]
    )


def build_todo_demo():
    default, set_default = use_state("basic")
    return MTTabs(
        {"defaultValue": default, "onChange": set_default},
        [
            MTTabsList([
                MTTabsTab({"value": "basic"}, "a simple todo list"),
                MTTabsTab({"value": "full"}, "A todo list with add/done/revert/delete support"),
            ]),
            MTTabsPanel({"value": "basic"},
                        MTPaper(
                            {"shadow": 'lg', "class": "m-2"},
                            MTScrollArea(
                                {"h": 200},
                                MTCodeHighlight(
                                    """todos, set_todos = use_state([])
def add_todo(e):
    todos.insert(0, e)
    set_todos(copy(todos))

return html.div(
    [
        MTInputX({ "sync": add_todo }),
        html.ul([html.li(v) for v in todos])
    ]
)
                        """)




                            ),
                        )),
            MTTabsPanel({"value": "full"},
                        MTPaper(
                            {"shadow": 'lg', "class": "m-2"},
                            MTScrollArea(
                                {"h": 200},
                                MTCodeHighlight("""
todos, set_todos = use_state([])

def add_todo(e):
    todos.insert(0, {"done": False, "value": e})
    set_todos(copy(todos))
    
def done_todo(i):
    def wrap(e):
        todos[i]["done"] = not todos[i]["done"]
        set_todos(copy(todos))
    return wrap
    
def del_todo(i):
    def wrap(e):
        todos and todos.pop(i) and set_todos(copy(todos))
    return wrap

return html.div(
    [
        MTInputX({ "sync": add_todo }),
        html.ul(
            [html.li({
                "onClick": done_todo(i),
                "onDoubleClick": del_todo(i),
                "style": {"text-decoration": v.get('done') and 'line-through'}
            }, v.get('value')) for i,v in enumerate(todos)]
        )
    ]
)
                                """)
                            ,

                            )

                        )),
        ]
    )


@component
def plot_home(option):
    return html.div(
        MTProvider(
        MTPaper(
            {"shadow": 'lg', "class": "mx-10 "},
            MTGrid(
                {"class": "pb-10", "columns": 12},
                [
                    MTGridCol(
                        {"span": 10, "offset": 1},
                        Markdown("""
# Hello Pythonistas!

This is a hobby project for using React & Python to build beautiful web pages! 

The project is using ReactPy as its backend and integrates with several fantastic libraries!

- Typescript UI
    - Mantine
    - Mantine DataTable
    - Tailwind CSS
    - ECharts
    - VegaLite
    - Marked
- Python UI
    - Tailwind CSS
    - ...

I hope this project will help easing your process of bringing your idea into the real world via Python.

#### Basics

You need to know the basic idea of ReactPy, like how to define the components.

To get a rough idea of how to write apps in ReactPy, take a look at this tiny Hello World application.

```python
from reactpy import component, html, run

@component
def hello_world():
    return html.h1("Hello, World!")

run(hello_world)
```

for RPySuite, only two params you need to take care of

- the first param is about the attributes or props
- the second one is about the content or children.

there is one interactive demo todo app below, **give it a try & have fun!**

#### How to install

as we use the latest version of ReactPy from github, you can uninstall it first(if already installed), and then

```bash
pip install rpysuite
```

if sth is missing, use pip to install it.

you can use different ways to run it , as it's an asgi app

here is the command to run the demo via granian

```bash
granian --interface asgi rpysuite.examples.main:app --port 8888  --workers 2 --threads 2
```

            """),
                        MTTitle({"order": 4}, "A Basic Todo!"),
                        build_todo_demo(),
                        MTText("1.type text in the input. 2. type enter to add to the list. 3. click the item to switch state. 4. double click the item to delete."),
                        render_real_todo(),
                    ),
                ]
            )
        )
    )
    )