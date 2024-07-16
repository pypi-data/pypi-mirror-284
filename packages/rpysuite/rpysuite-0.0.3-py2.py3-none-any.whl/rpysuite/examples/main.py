from rpysuite.examples.data import menu, views, icons
from rpysuite.examples.shell import AppShell

app = AppShell(
    menu = menu,
    views = views,
    title = 'RPySuite Works!',
    icons = icons
).app

# run(render)