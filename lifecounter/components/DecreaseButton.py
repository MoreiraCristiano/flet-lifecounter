from flet import UserControl, Container, ElevatedButton


class DecreaseButton(UserControl):
    def __init__(self, life_points, lp_container, rotate):
        super().__init__()
        self.life_points = life_points
        self.lp_container = lp_container
        self.rotate = rotate

    def build(self):
        return Container(
            ElevatedButton(
                f'-{self.life_points}',
                rotate=self.rotate,
                scale=1.3,
                on_click=lambda e: self.lp_container.decrement_life(
                    e, self.life_points
                ),
            ),
        )
