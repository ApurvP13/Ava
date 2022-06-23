from turtle import width
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

		self.rows = 3
		self.padding=15

		self.add_widget(Label(text = "Welcome To AVA", size_hint =(.5, .95), font_name = "Georgia", font_size = "70", color = [225/255, 112/255, 85/255, 1.0]))
		self.add_widget(Label(text="Your personal assistant at your service.",size_hint =(.5, .35), font_name = "Georgia", font_size = "35", color = [225/255, 112/255, 85/255, 1.0] ))
		self.continue_butt = Button(text = "CONTINUE",size_hint =(1, .30), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgia", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
		self.continue_butt.bind(on_press = self.nextPage)
		self.add_widget(self.continue_butt)
		

	def nextPage(self, instance):
		pa_app.screen_manager.current = "input"

        

class InputPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 3
		self.padding=15
		self.spacing=10

		self.add_widget(Label(text = "Type Your Input Here", font_name = "Georgia", font_size = "60", color = [225/255, 112/255, 85/255, 1.0]))



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