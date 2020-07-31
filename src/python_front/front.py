import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require('1.01.1')
from kivy.uix.button import Button
import requests
import ast

class ConnectPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text='username:'))
		self.username = TextInput(multiline=False,pos=(30,30))
		self.add_widget(self.username)
		
		self.add_widget(Label(text='password:'))
		self.password = TextInput(multiline=False)
		self.add_widget(self.password)

		self.register = Button(text='register new user')
		self.add_widget(self.register)

		self.signin = Button(text='sign in')
		self.signin.bind(on_press=self.sign_in)
		self.add_widget(self.signin)

	def sign_in(self, instance):
		username = self.username.text
		password = self.password.text
		url = 'http://127.0.0.1:5000/login'
		response = requests.post(url, data={'username':username, 'password':password}).content
		response = response.decode('UTF-8')
		response = ast.literal_eval(response)
		print(response)

		if response['access']:
			return Sign_In_Page()

class Sign_In_Page(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.add_widget(Label(text='Your are signed in'))


class Flex_Play(App):
	def build(self):
		return ConnectPage()

if __name__ == '__main__':
	Flex_Play().run()