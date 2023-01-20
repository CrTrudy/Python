
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.metrics import dp


class Feld(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 9
        self.rows = 9
        self.clear_widgets()
        for i in range(1, 82):
            button = Button(text=str(i), size=(dp(40), dp(40)), size_hint=(None, None))
            self.add_widget(button)

    pass