from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
import requests

screen_helper = """
ScreenManager:
	LoginScreen:
	PlayerHomeScreen:

<LoginScreen>:
	name : 'login'
	MDLabel:
		text:'Welcome Champion!!!'
		halign:'center'
		theme_text_color:'Secondary'
		font_style:'H3'
		pos_hint:{'center_x':0.5,'center_y':0.65}
	MDFloatingActionButton:
		icon:'soccer'
		pos_hint:{'center_x':0.5, 'center_y':0.13}
		on_press:root.manager.current = 'profile'
	MDTextField:
		text:'username'
		pos_hint:{'center_x':0.5,'center_y':0.4}
		size_hint_x:None
		width:300
	MDTextField:
		text:'password'
		pos_hint:{'center_x':0.5,'center_y':0.3}
		size_hint_x:None
		width:300

<PlayerHomeScreen>:
	name: 'profile'
	MDLabel:
		text:root.generate_name()
		halign:'center'
		theme_text_color:'Secondary'
		font_style:'H3'
		pos_hint:{'center_x':0.5,'center_y':0.65}
"""

class LoginScreen(Screen):
	def login(self):
		url = 'http://127.0.0.1:5000/login'
		obj = {'username':'deveshdatwani','password':'devesh'}
		response = requests.post(url=url,data=obj).json()
		if response[0]['access']:
			return str(response[0]['access'])

	def pri(self,check):
		print(check)		

class PlayerHomeScreen(Screen):
	def generate_name(self):
		

		return 'hello'
		
	
	pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(PlayerHomeScreen(name='profile'))

class Front(MDApp):

	def go():
		print('jello')

	name = StringProperty("")

	def build(self):
		screen = Builder.load_string(screen_helper)
		return screen

if __name__ == '__main__':
	
	Front().run()
