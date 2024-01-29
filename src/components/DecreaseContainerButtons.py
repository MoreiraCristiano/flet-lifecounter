from flet import UserControl, Row, MainAxisAlignment
from .DecreaseButton import DecreaseButton


class DecreaseContainerButtons(UserControl):
    def __init__(self, options, lp_container):
        super().__init__()
        self.options = options
        self.lp_container = lp_container

    def build(self):
        return Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                DecreaseButton(option, lp_container=self.lp_container)
                for option in self.options
                if self.options is not None
            ],
        )
