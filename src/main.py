import flet as ft
from flet_core.page import ThemeMode
from components.LifePointsContainer import LifePointsContainer
from components.DecreaseContainerButtons import DecreaseContainerButtons
from math import pi


ROTATE_90 = pi / 2


def main(page: ft.Page):
    page.window_width = 480
    # page.window_height = 840
    page.title = 'Simple life points counter'
    page.window_resizable = False
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.theme_mode = ThemeMode.DARK
    page.update()

    lp_containers = (
        LifePointsContainer(20, pi, 0, page),
        LifePointsContainer(20, 0, 1, page),
    )

    app = ft.Column(
        [
            DecreaseContainerButtons((5, 10, 15), lp_containers[0], pi),
            lp_containers[0],
            ft.Divider(color='#505050', thickness=2),
            lp_containers[1],
            DecreaseContainerButtons((5, 10, 15), lp_containers[1], 0),
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    page.add(app)


ft.app(main)
