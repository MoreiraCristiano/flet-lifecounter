import flet as ft


class DecreaseButton(ft.UserControl):
    def __init__(self, life_points):
        super().__init__()
        self.life_points = life_points

    def build(self):
        return ft.Container(
            ft.ElevatedButton(f'-{self.life_points}', scale=1.2), padding=20
        )


class DecreaseContainerButtons(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            # expand=True,
            controls=[
                DecreaseButton('5'),
                DecreaseButton('10'),
                DecreaseButton('15'),
            ],
        )


class LifePointsContainer(ft.UserControl):
    def __init__(self, initial_life_points):
        super().__init__()
        self.initial_life_points = initial_life_points
        self.life_points_counter = ft.Text(
            value=self.initial_life_points, text_align='center', size=70
        )

    def build(self):
        return ft.Row(
            # expand=True,
            alignment="center",
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=self.decrement_life_by_one),
                self.life_points_counter,
                ft.IconButton(ft.icons.ADD, on_click=self.increment_life_by_one),
            ],
        )

    def decrement_life_by_one(self, event):
        self.life_points_counter.value -= 1
        self.update()

    def increment_life_by_one(self, event):
        self.life_points_counter.value += 1
        self.update()


def main(page: ft.Page):
    page.window_width = 480
    page.window_height = 800
    # page.window_always_on_top = True
    page.vertical_alignment = 'center'
    page.update()

    app = ft.Column(
        [
            DecreaseContainerButtons(),
            LifePointsContainer(20),
            ft.Divider(color='white'),
            LifePointsContainer(25),
            DecreaseContainerButtons(),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        expand=True,
    )

    page.add(app)


ft.app(main)
