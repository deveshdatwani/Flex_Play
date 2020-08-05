from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import requests
from kivy.properties import StringProperty,ListProperty
from kivy.config import Config

Config.set('graphics','width','500')
Config.set('graphics','resizable','0')
Config.set('graphics', 'height','600')

class MainWindow(Screen):
	
	username = StringProperty('')
	firstname = StringProperty('')
	email = StringProperty('')
	phonenumber = StringProperty('')
	
	def login(self,username,password):
		url = 'http://127.0.0.1:5000/login'
		obj = {'username':username,'password':password}
		response = requests.post(url=url, data = obj)
		self.username = username
		self.firstname = response.json()[1]['firstname']
		self.email = response.json()[1]['email']
		self.phonenumber = str(response.json()[1]['phonenumber'])
		print(response.json()[1])
		return response.json()[0]['access']
	pass

class PlayerHome(Screen):
	
	username = StringProperty('')
	firstname = StringProperty('')
	email = StringProperty('')
	phonenumber = StringProperty('')
	groupplayers = ListProperty('')

	def go_to_group_home(self,username):

		url = 'http://127.0.0.1:5000/group_home'
		obj = {'username':username}
		response = requests.post(url=url, data = obj)
		self.groupplayers = response.content.decode('utf-8').split(',')

	pass

class WindowManager(ScreenManager):
	pass 

class GroupHome(Screen):
	username = StringProperty('')
	groupplayers = ListProperty('')

	pass

class CreateGroupEvent(Screen):

	username = StringProperty('')

	def create_event(self,username,player,eventarena,time,date,gameplayduration,latitude,longitude):

		username = username
		url = 'http://127.0.0.1:5000/group_home'
		obj = {'username':username,
			   'player':username,
			   'latitude':latitude,
			   'longitude':longitude,
			   'daytime':daytime,
			   'team':team,
			   'eventarena':eventarena,
			   'privacy':1,
			   ''   }
		response = requests.post(url=url, data = obj)

		pass
	
	pass


kv = Builder.load_file('app.kv')

class FlexFront(App):
	def build(self):
		return kv 

if __name__ == '__main__':
	FlexFront().run()