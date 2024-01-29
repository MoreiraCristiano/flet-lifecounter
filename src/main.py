import flet as ft
from components.LifePointsContainer import LifePointsContainer
from components.DecreaseContainerButtons import DecreaseContainerButtons


def main(page: ft.Page):
    page.window_width = 480
    page.window_height = 800
    page.title = 'Simple life points counter'
    page.window_resizable = False
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.update()

    lp_containers = (LifePointsContainer(20), LifePointsContainer(20))

    app = ft.Column(
        [
            DecreaseContainerButtons((5, 10, 15), lp_containers[0]),
            lp_containers[0],
            ft.Divider(color='white'),
            lp_containers[1],
            DecreaseContainerButtons((5, 10, 15), lp_containers[1]),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        expand=True,
    )

    page.add(app)


ft.app(main)
