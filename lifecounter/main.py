from flet import Page, Text, app, ElevatedButton
from flet_core.page import ThemeMode
from components.ScreenLifeCounter import ScreenLifeCounter
from utils.routes import view_pop, route_change
from math import pi


def main(page: Page):
    page.window_width = 480
    # page.window_height = 840
    page.title = 'Simple life points counter'
    page.window_resizable = False
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.theme_mode = ThemeMode.DARK
    main_page = ScreenLifeCounter(page)

    page.update()

    page.on_route_change = lambda r: route_change(r, page, main_page)
    page.on_view_pop = lambda v: view_pop(v, page)

    page.go('/lifecounter')


app(main)
