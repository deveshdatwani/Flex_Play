from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from kivy.uix.recycleview import RecycleView
import requests


class Front(MDApp):

    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        front_label = MDLabel(text='Welcome Champion!!!',
                      halign='center',
                      theme_text_color='Secondary',
                      font_style='H3',
                      pos_hint={'center_x':0.5,'center_y':0.65})
        button_flat = MDFloatingActionButton(icon='soccer',
                            pos_hint={'center_x':0.5, 'center_y':0.1},
                            on_release=self.login)
        self.username = MDTextField(text='username',
                      pos_hint={'center_x':0.5,'center_y':0.4},
                      size_hint_x=None,width=300)
        self.password = MDTextField(text='password',
                      pos_hint={'center_x':0.5,'center_y':0.3},
                      size_hint_x=None,width=300)
        
        self.screen.add_widget(self.password)
        self.screen.add_widget(self.username)
        self.screen.add_widget(button_flat)
        self.screen.add_widget(front_label)

        return self.screen

    def login(self,obj):
        self.screen.clear_widgets()
        myobj = {'username':self.username.text, 'password':self.password.text}
        url = 'http://127.0.0.1:5000/login'
        response = requests.post(url=url, data = myobj)
       
        if response.json()[0]['access']:
            self.player_info = response.json()[1]
            front_label = MDLabel(text='Welcome {}'.format(self.player_info['firstname']),
                                    halign='center',theme_text_color='Secondary',
                                    font_style='H4',
                                    pos_hint={'center_x':0.5,'center_y':0.88}) 
            phone_label = MDLabel(text='{}'.format(self.player_info['phonenumber']),
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Subtitle1',
                                    pos_hint={'center_x':0.8,'center_y':0.72}) 
            email_label = MDLabel(text='{}'.format(self.player_info['email']),
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Subtitle1',
                                    pos_hint={'center_x':0.8,'center_y':0.69})
            username_label = MDLabel(text='username:\n{}'.format(self.player_info['username']),
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Subtitle1',
                                    pos_hint={'center_x':0.2,'center_y':0.7})             
            group_button = MDFloatingActionButton(icon='account-group',
                                    pos_hint={'center_x':0.2, 'center_y':0.15},
                                    on_release=self.group_home,
                                    background_palette='Green')
            find_event_button = MDFloatingActionButton(icon='soccer',
                                    pos_hint={'center_x':0.5, 'center_y':0.15},
                                    on_release=self.find_events)
            create_event_button = MDFloatingActionButton(icon='soccer-field',
                                    pos_hint={'center_x':0.8, 'center_y':0.15},
                                    on_release=self.create_event)
            group_button_label = MDLabel(text='Group',
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Caption',
                                    pos_hint={'center_x':0.2,'center_y':0.085}) 
            find_event_button_label = MDLabel(text='Find Event',
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Caption',
                                    pos_hint={'center_x':0.5,'center_y':0.085}) 
            create_event_button_label = MDLabel(text='Create Event',
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Caption',
                                    pos_hint={'center_x':0.8,'center_y':0.085}) 


            self.screen.add_widget(front_label)
            self.screen.add_widget(group_button)
            self.screen.add_widget(find_event_button)
            self.screen.add_widget(create_event_button)
            self.screen.add_widget(phone_label)
            self.screen.add_widget(username_label)
            self.screen.add_widget(email_label)
            self.screen.add_widget(group_button_label)
            self.screen.add_widget(find_event_button_label)
            self.screen.add_widget(create_event_button_label)
                
        else:
            display_response = response.json()[1]
            front_label = MDLabel(text=display_response,halign='center',theme_text_color='Secondary',font_style='H3',pos_hint={'center_x':0.5,'center_y':0.65})

            self.screen.add_widget(front_label)
        

        return self.screen

    def group_home(self,obj): 
        super(Front,self).__init__(**kwargs)  
        self.screen.clear_widgets()
        front_label = MDLabel(text='Team: {}'.format(self.player_info['teamname']),
                            halign='center',theme_text_color='Secondary',
                            font_style='H5',
                            pos_hint={'center_x':0.5,'center_y':0.88})
        myobj = {'username':self.player_info['username']}
        url = 'http://127.0.0.1:5000/group_home'
        group_response = requests.post(url=url,data=myobj).content
        group_response = group_response.decode("utf-8")
        group_response = group_response.split(',')
        group_response = ' '.join(group_response)
        group_response = group_response.replace(' ','\\n')
        print(group_response)
        view = MDLabel(text='{}'.format(group_response),
                        pos_hint={'center_x':0.5,'center_y':0.7},
                        theme_text_color='Secondary',
                        halign='center')
        group_events_button = MDFloatingActionButton(icon='soccer',
                                    pos_hint={'center_x':0.2, 'center_y':0.15},
                                    on_release=self.group_events,
                                    background_palette='Green')
        create_group_event_button = MDFloatingActionButton(icon='soccer-field',
                                    pos_hint={'center_x':0.8, 'center_y':0.15},
                                    on_release=self.create_event)
        group_events_button_label = MDLabel(text='Group Events',
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Caption',
                                    pos_hint={'center_x':0.2,'center_y':0.085}) 
        create_group_event_button_label = MDLabel(text='Create Group Event',
                                    halign='center',theme_text_color='Secondary',
                                    font_style='Caption',
                                    pos_hint={'center_x':0.8,'center_y':0.085}) 
        self.screen.add_widget(group_events_button)
        self.screen.add_widget(create_group_event_button)
        self.screen.add_widget(group_events_button_label)
        self.screen.add_widget(create_group_event_button_label)
        self.screen.add_widget(view)
        self.screen.add_widget(front_label)

        return self.screen

    def group_events(self,obj):
        self.screen.clear_widgets()
        print('button pressed')
        label = MDLabel(text='Group Events',
                        halign='center',theme_text_color='Secondary',
                        font_style='Caption',
                        pos_hint={'center_x':0.8,'center_y':0.085}) 
        
        self.screen.add_widget(label)

        return self.screen

    def create_event(self,obj):
        print('hello')
        

    def group_events(self,obj):
        pass

    def group_event_home(self,obj): 
        pass

    def find_event(self,obj):
        pass

    def find_events(self,obj):
        pass

    def create_event(self,obj):
        pass



Front().run()
