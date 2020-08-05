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
	team = StringProperty('')
	
	def login(self,username,password):
		url = 'http://127.0.0.1:5000/login'
		obj = {'username':username,'password':password}
		response = requests.post(url=url, data = obj)
		self.username = username
		self.firstname = response.json()[1]['firstname']
		self.email = response.json()[1]['email']
		self.phonenumber = str(response.json()[1]['phonenumber'])
		self.team = response.json()[1]['email']
		
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
		print(type(self.groupplayers))

	pass

class WindowManager(ScreenManager):
	pass 

class GroupHome(Screen):
	username = StringProperty('')
	groupplayers = ListProperty('')
	response = StringProperty('')
	groupevents = StringProperty('')

	def see_group_events(self,username):
		url = 'http://127.0.0.1:5000/group_events'
		obj = {'username':username}
		response = requests.post(url=url, data = obj)
		response = response.content.decode('utf-8')
		self.groupevents = response

	pass

class CreateGroupEvent(Screen):

	username = StringProperty('')
	team = StringProperty('')

	def create_event(self,username,eventarena,daytime,gameplayduration,latitude,longitude,team):

		url = 'http://127.0.0.1:5000/create_event'
		obj = {'creater':username,
			   'player':username,
			   'eventarena':eventarena,
			   'daytime':daytime,
			   'gameplaytime':gameplayduration,
			   'latitude':latitude,
			   'longitude':longitude,
			   'team':team,
			   'privacy':1
			    }
		pass
	
	pass

class SeeGroupEvents(Screen):

	groupevents = StringProperty('')

	pass

class CreateEvent(Screen):

	team = StringProperty('')
	username = StringProperty('')

	pass

kv = Builder.load_file('app.kv')

class FlexFront(App):
	def build(self):
		return kv 

if __name__ == '__main__':
	FlexFront().run()