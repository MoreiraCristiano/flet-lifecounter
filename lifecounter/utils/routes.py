import flet as ft
from components.ScreenLifeCounter import ScreenLifeCounter


def route_change(route, page, default_view):
    '''
    Description: Navigate between configured routes
    Parameters: route: callback | page: app page to handle | default_view: The control for route '/'
    Return: Null
    '''
    page.views.clear()
    page.views.append(ft.View('/', [default_view]))

    if page.route == '/lifecounter':
        screenLifeCounter = ScreenLifeCounter(page)
        page.views.append(screenLifeCounter.build())

    page.update()


def view_pop(view, page):
    '''
    Description: Navigate between pages browser
    Parameters: view: callback mandatory parameter | page: the app page to handle
    Return: Null
    '''
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
