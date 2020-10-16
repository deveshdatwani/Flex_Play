from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
from kivy.properties import StringProperty,ListProperty,ObjectProperty
from kivy.config import Config
from textwrap import wrap
from kivy.clock import mainthread
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.clock import mainthread

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
		self.team = response.json()[1]['teamname']

		return response.json()[0]['access']
	pass

class PlayerHome(Screen):

	username = StringProperty('')
	firstname = StringProperty('')
	email = StringProperty('')
	phonenumber = StringProperty('')
	groupplayers = ListProperty('')
	yourevents = ListProperty('')
	yournotifications = ListProperty('')

	def go_to_group_home(self,username):

		url = 'http://127.0.0.1:5000/group_home'
		obj = {'username':username}
		response = requests.post(url=url, data = obj)
		self.groupplayers = response.content.decode('utf-8').split(',')

	def see_your_events(self,username):

		url = 'http://127.0.0.1:5000/your_events'
		obj = {'username':username}
		response = requests.post(url=url, data=obj)
		self.yourevents = response.content

	def see_your_notifications(self,username):

		url = 'http://127.0.0.1:5000/see_your_notifications'
		obj = {'username':username}
		response = requests.post(url=url, data = obj)
		notifications = response.content.decode('utf-8')
		self.yournotifications = notifications.split('--')

	pass

class WindowManager(ScreenManager):

	pass

class GroupHome(Screen):

	username = StringProperty('')
	groupplayers = ListProperty('')
	groupevents = ListProperty('')
	yournotifications = ListProperty('')

	def see_group_events(self,username):

		event_list = []
		all_events = []
		url = 'http://127.0.0.1:5000/group_events'
		obj = {'username':username}
		response = requests.post(url=url, data = obj)
		response = response.content.decode('utf-8')
		response = response.replace(',', '\t')
		event_list =response.split('\t')
		self.groupevents = [str(event_list[i:i+3]) for i in range(0,len(event_list),4)]

		pass

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

		requests.post(url=url, data=obj)

		pass

	pass

class SeeGroupEvents(Screen):

	groupevents = ListProperty('')
	eventplayers = ListProperty('')
	eventname = StringProperty('')
	eventdate = StringProperty('')

	@mainthread
	def on_enter(self):
		for i,event in enumerate(self.groupevents):
			print(event)
			event = Button(text=event,pos=(60,200+(i*100)),size_hint=(0.8,0.1))
			self.ids.seeallgroupevents.add_widget(event)
			event.bind(on_press=self.sayhi)

	def sayhi(self,what):

		events = what.text.split(',')
		creater = events[0]
		daytime = events[2]
		creater = creater.split("'")[1]
		daytime = daytime.split("'")[1]
		url = 'http://127.0.0.1:5000/see_event_details'
		obj = {'creater':creater, 'daytime':daytime}
		response = requests.post(url=url, data = obj)
		self.eventplayers = response.content.decode('utf-8').split(',')
		self.manager.current = 'SeeEventDetails'
		self.eventname = creater + "'s " + 'Event'
		self.eventdate = "Event Date: " + daytime

	pass

class CreateEvent(Screen):

	team = StringProperty('')
	username = StringProperty('')

	def create_event(self,username,eventarena,daytime,gameplayduration,latitude,longitude,team):

		url = 'http://127.0.0.1:5000/create_event'
		obj = obj = {'creater':username,
			   'player':username,
			   'eventarena':eventarena,
			   'daytime':daytime,
			   'gameplaytime':gameplayduration,
			   'latitude':latitude,
			   'longitude':longitude,
			   'team':team,
			   'privacy':0
			    }

		requests.post(url=url,data=obj)

		pass

	pass

class FindEvents(Screen):

	pass

class SeeEventDetails(Screen):

	eventplayers = ListProperty('')
	eventname = StringProperty('')
	eventdate = StringProperty('')

	pass

class YourEvents(Screen):

	yourevents = ListProperty('')

	pass

class YourNotifications(Screen):

	yournotifications = ListProperty('')

	@mainthread
	def on_enter(self):
		for i, event in enumerate(self.yournotifications):
			print(event)
			event = Button(text= 'Join ' + event,pos=(100, 100+(i*50)), size_hint=(0.5,0.06))
			accept = Button(text='Accept',pos=(350, 100+(i*50)),size_hint=(0.1,0.06))
			reject = Button(text= 'Reject',pos=(400, 100+(i*50)),size_hint=(0.1,0.06))
			self.ids.seeyournotifications.add_widget(event)	
			self.ids.seeyournotifications.add_widget(accept)
			self.ids.seeyournotifications.add_widget(reject)
	pass

class InvitePlayers(Screen):

	username = StringProperty('')
	team = StringProperty('')

	def invite_player(self,invitor,team,invited):

		url = 'http://127.0.0.1:5000/invite_player'
		obj = {'invitor':invitor, 'invited':invited, 'team':team}
		requests.post(url=url, data=obj)
	
	pass

kv = Builder.load_file('app.kv')

class FlexFront(App):

	def build(self):
		
		return kv 

if __name__ == '__main__':
	FlexFront().run()
