import flet as ft
from components.LifePointsContainer import LifePointsContainer
from components.DecreaseContainerButtons import DecreaseContainerButtons
from math import pi


ROTATE_90 = pi / 2


def main(page: ft.Page):
    page.window_width = 480
    page.window_height = 840
    page.title = 'Simple life points counter'
    page.window_resizable = False
    page.window_maximizable = False
    page.vertical_alignment = 'center'

    page.update()

    lp_containers = (LifePointsContainer(20, pi, 0), LifePointsContainer(20, 0, 1))

    app = ft.Column(
        [
            DecreaseContainerButtons((5, 10, 15), lp_containers[0], pi),
            lp_containers[0],
            ft.Divider(color='#505050', thickness=2),
            lp_containers[1],
            DecreaseContainerButtons((5, 10, 15), lp_containers[1], 0),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    page.add(app)


ft.app(main)
