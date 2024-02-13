from flet import (
    Row,
    IconButton,
    icons,
    AlertDialog,
    Column,
    TextField,
    ElevatedButton,
    MainAxisAlignment,
    UserControl,
    Text,
    KeyboardType,
    FontWeight,
)


class LifePointsContainer(UserControl):
    def __init__(self, initial_life_points, rotate):
        super().__init__()
        self.initial_life_points = initial_life_points
        self.life_points_counter = Text(
            value=self.initial_life_points,
            text_align='center',
            size=150,
            weight=FontWeight.W_300,
            rotate=rotate,
        )

    def set_initial_life_points(self, event):
        initial_life_field = TextField(
            label="Initial life points",
            keyboard_type=KeyboardType.NUMBER,
            autofocus=True,
        )

        def set_initial_life(event, initial_life):
            try:
                self.life_points_counter.value = int(initial_life)
                event.page.close_dialog()
                self.update()
            except ValueError:
                print('Inserir numeros e nao char')

        dlg_modal = AlertDialog(
            modal=True,
            title=Text("Life points"),
            content=Column([initial_life_field], tight=True),
            actions=[
                ElevatedButton(
                    "Yes",
                    on_click=lambda e: set_initial_life(e, initial_life_field.value),
                ),
                ElevatedButton("No", on_click=lambda e: e.page.close_dialog()),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        event.page.show_dialog(dlg_modal)

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

    def build(self):
        return Column(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Row(
                    controls=[
                        IconButton(
                            icons.REMOVE,
                            on_click=self.decrement_life_by_one,
                            icon_size=40,
                            expand=True,
                        ),
                        self.life_points_counter,
                        IconButton(
                            icons.ADD,
                            on_click=self.increment_life_by_one,
                            icon_size=40,
                            expand=True,
                        ),
                    ],
                    alignment='center',
                ),
                Row(
                    controls=[
                        IconButton(
                            icons.EDIT,
                            on_click=self.set_initial_life_points,
                        )
                    ],
                    alignment='center',
                ),
            ],
        )
