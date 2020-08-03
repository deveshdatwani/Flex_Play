from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty


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
		on_release:[lambda x: app.go()]
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
		text:'Hey'
		halign:'center'
		theme_text_color:'Secondary'
		font_style:'H3'
		pos_hint:{'center_x':0.5,'center_y':0.65}
"""

class LoginScreen(Screen):
	def name_gen(self):
		print('hello')
	pass
	

class PlayerHomeScreen(Screen):
	def generate_name(self):
		elf = 'Devesh'

		return elf
	
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
