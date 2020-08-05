from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import requests
from kivy.uix.screenmanager import ScreenManager

class Front(MDApp):

	def login_page(self):
		screen = Screen()
		theme_cls.primary_palette = 'Green'
		theme_cls.theme_style = 'Dark'
		front_label = MDLabel(text='Welcome Champion!!!',
				      halign='center',
				      theme_text_color='Secondary',
				      font_style='H3',
				      pos_hint={'center_x':0.5,'center_y':0.65})
		button_flat = MDFloatingActionButton(icon='soccer',
						    pos_hint={'center_x':0.5, 'center_y':0.13},
						    on_release=self.login)
		username = MDTextField(text='username',
				      pos_hint={'center_x':0.5,'center_y':0.4},
				      size_hint_x=None,width=300)
		password = MDTextField(text='password',
				      pos_hint={'center_x':0.5,'center_y':0.3},
				      size_hint_x=None,width=300)
		screen.add_widget(password)
		screen.add_widget(username)
		screen.add_widget(button_flat)
		screen.add_widget(front_label)

		return screen

#	def login(self,obj):
#		screen2 = Screen()
#		myobj = {'username':self.username.text, 'password':self.password.text}
#		response = requests.post('http://127.0.0.1:5000/login', data = myobj)
#		
#		if response.json()[0]['access']:
#			front_label = MDLabel(text='Welcome',
#					      halign='center',
#					      theme_text_color='Secondary',
#					      font_style='H3',
#					      pos_hint={'center_x':0.5,'center_y':0.65})

#			screen2.add_widget(front_label)
		
#		return screen2


if __name__ == '__main__':
	Front().run()
