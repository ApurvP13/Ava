import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import wolframalpha as wolfaplha
import wikipedia 

from kivy.core.audio import SoundLoader




from kivy.core.window import Window
Window.clearcolor = (246/255, 239/255, 233/255, 1)


class IntroPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 3
		self.padding=15

		#Affable Virtual Assistant
		self.add_widget(Label(text = "Welcome To AVA", size_hint =(.5, .95), font_name = "Georgia", font_size = "70", color = [225/255, 112/255, 85/255, 1.0]))
		self.add_widget(Label(text="(Your personal assistant at your service.)",size_hint =(.5, .35), font_name = "Georgia", font_size = "35", color = [225/255, 112/255, 85/255, 1.0] ))
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

		self.add_widget(Label(text = "Enter what you want to know about", font_name = "Georgia", font_size = "46", color = [225/255, 112/255, 85/255, 1.0]))


		self.input_text = TextInput(multiline = "false", font_size = 30, background_color = (232/255, 214/255, 203/255, 1), size_hint =(.5, .5), padding_x=[150,200], font_name = "Arial", foreground_color = [61/255, 61/255, 61/255, 1.0])
		self.add_widget(self.input_text)

		self.result_butt = Button(text = "ANSWER",size_hint =(.25, .25), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgia", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
		self.result_butt.bind(on_press = self.result_gen)
		self.add_widget(self.result_butt)


	def result_gen(self, instance):
		in_text = self.input_text.text

		if "are you" in in_text:
			print("help me")
			pa_app.page3.update_info("I am doing fine :D") #morse code for help me 
			sound  = SoundLoader.load("help.wav")
			sound.volume = 0.8
			sound.play()


		else:
			#for using the wolfram alpha api
			app_id = 'GK5TVX-Q3KEU8J4HQ'
			client = wolfaplha.Client(app_id)
			result = client.query(in_text)
			try:
				answer = next(result.results).text
				print(answer)
				pa_app.page3.update_info(answer)
			except:
				try:
					result = wikipedia.summary(in_text, sentences=5)
					pa_app.page3.update_info(result)
				except:
					result = "invalid question/no data available"
					pa_app.page3.update_info(result)
				
		pa_app.screen_manager.current = "result"
		

class ResultPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 2
		self.padding=15
		self.spacing=10

		self.result_lbl = Label(text = "", font_name = "Georgia", font_size = "60", color = [61/255, 61/255, 61/255, 1.0])
		self.result_lbl.bind(width=self.update_text_width)
		self.add_widget(self.result_lbl)

		self.back_butt = Button(text = "BACK",size_hint =(.20, .20), background_normal="",background_color = [225/255, 112/255, 85/255, 1.0], font_name = "Georgia", color = [255/255, 234/255, 167/255,1.0], font_size =40 )
		self.back_butt.bind(on_press = self.back_in)
		self.add_widget(self.back_butt)

	def update_info(self,text):
		self.result_lbl.text = text

	def update_text_width(self, *_):
		self.result_lbl.text_size= (self.result_lbl.width*0.9, None)

	def back_in(self, instance):
		pa_app.screen_manager.current = "input"

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

		self.page3 = ResultPage()
		screen  =Screen(name = "result")
		screen.add_widget(self.page3)
		self.screen_manager.add_widget(screen)

		return self.screen_manager

if __name__ == "__main__":
    pa_app = PAApp()
    pa_app.run()