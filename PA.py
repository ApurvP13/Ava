import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.core.window import Window
Window.clearcolor = (246/255, 239/255, 233/255, 1)


class IntroPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 2

		self.add_widget(Label(text = "Welcome To AVA", font_name = "Georgia", font_size = "60", color = [225/255, 112/255, 85/255, 1.0]))
		self.continue_butt = Button(text = "CONTINUE",size_hint =(.5, .25), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgia", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
		self.continue_butt.bind(on_press = self.nextPage)
		self.add_widget(self.continue_butt)

	def nextPage(self, instance):
		pa_app.screen_manager.current = "input"

        

class InputPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 3

		self.add_widget(Label(text = "Type Your Input Here", font_name = "Georgia", font_size = "60", color = [225/255, 112/255, 85/255, 1.0]))

		self.add_widget(TextInput(multiline = "false", font_size = 30, background_color = (232/255, 214/255, 203/255, 1), size_hint =(.5, .5), padding_x=[200,200], font_name = "Arial", foreground_color = [61/255, 61/255, 61/255, 1.0]))

		self.result_butt = Button(text = "RESULT",size_hint =(.25, .25), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgia", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
		self.add_widget(self.result_butt)

class PAApp(App):
	def build(self):
		self.screen_manager = ScreenManager()

		self.page1 = IntroPage()
		screen = Screen(name = "intro")
		screen.add_widget(self.page1)
		self.screen_manager.add_widget(screen)

		self.page2 = InputPage()
		screen = Screen(name = "input")
		screen.add_widget(self.page2)
		self.screen_manager.add_widget(screen)

		return self.screen_manager

if __name__ == "__main__":
    pa_app = PAApp()
    pa_app.run()