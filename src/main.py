import flet as ft


class DecreaseButton(ft.UserControl):
    def __init__(self, life_points, lp_container):
        super().__init__()
        self.life_points = life_points
        self.lp_container = lp_container

    def build(self):
        return ft.Container(
            ft.ElevatedButton(
                f'-{self.life_points}',
                scale=1.2,
                on_click=lambda e: self.lp_container.decrement_life(
                    e, self.life_points
                ),
            ),
            padding=20,
        )


class DecreaseContainerButtons(ft.UserControl):
    def __init__(self, options, lp_container):
        super().__init__()
        self.options = options
        self.lp_container = lp_container

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                DecreaseButton(option, lp_container=self.lp_container)
                for option in self.options
                if self.options is not None
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

    def increment_life_by_one(self, event):
        self.life_points_counter.value += 1
        self.update()

    def decrement_life_by_one(self, event):
        if self.life_points_counter.value <= 0:
            self.life_points_counter.value = 0
            self.update()
        else:
            self.life_points_counter.value -= 1
            self.update()

    def decrement_life(self, event, decrement_value):
        if self.life_points_counter.value - decrement_value <= 0:
            self.life_points_counter.value = 0
            self.update()
        else:
            self.life_points_counter.value -= decrement_value
            self.update()


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
