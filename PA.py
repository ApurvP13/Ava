
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button


class IntroPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2
# adding the label
        self.add_widget(Label(text = "Welcome To AVA"))
#adding the button
        self.continue_butt = Button(text = "continue")
        self.add_widget(self.continue_butt)

class PAApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.page1 = IntroPage()
        screen = Screen(name="intro")
        screen.add_widget(self.page1)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    pa_app = PAApp()
    pa_app.run()
