import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.core.window import Window
Window.clearcolor = (246/255, 239/255, 233/255, 1)


class IntroPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2
# adding the labels
        self.add_widget(Label(text = "Welcome To AVA", font_name = "Georgia", font_size = "60", color = [225/255, 112/255, 85/255, 1.0]))
#adding the button
        self.continue_butt = Button(text = "CONTINUE",size_hint =(.5, .25), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgiab", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
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