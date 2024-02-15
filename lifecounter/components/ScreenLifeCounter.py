from flet import UserControl, View, Divider, Column, MainAxisAlignment, Text, Row
from components.DecreaseContainerButtons import DecreaseContainerButtons
from components.LifePointsContainer import LifePointsContainer
from math import pi


class ScreenLifeCounter(UserControl):
    def __init__(self, page):
        super().__init__()
        self.lp_containers = (
            LifePointsContainer(20, pi, 0, page),
            LifePointsContainer(20, 0, 1, page),
        )

    def build(self):
        return View(
            '/lifecounter',
            [
                Column(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        DecreaseContainerButtons(
                            (5, 10, 15), self.lp_containers[0], pi
                        ),
                        self.lp_containers[0],
                        Divider(color='#505050', thickness=2),
                        self.lp_containers[1],
                        DecreaseContainerButtons((5, 10, 15), self.lp_containers[1], 0),
                    ],
                )
            ],
        )
