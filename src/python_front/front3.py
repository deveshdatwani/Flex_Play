import GlobalShared
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_string("""
<ScreenOne>:
   BoxLayout:
      orientation:'vertical'
      Label:
            text: 'I am ScreenOne'
      Label:
            id: lbl1
      Button:
            text: 'Read'
            on_press: root.press_read()
      Button:
            text: 'Change'
            on_press: root.press_change()
      Button:
            text: 'Go to ScreenTwo'
            on_press: app.sm.current = "screen_2"
<ScreenTwo>:
   BoxLayout:
      orientation:'vertical'
      Label:
            text: 'I am ScreenTwo'
      Label:
            id: lbl2
      Button:
            text: 'Read'
            on_press: root.press_read()
      Button:
            text: 'Change'
            on_press: root.press_change()
      Button:
            text: 'Go to ScreenOne'
            on_press: app.sm.current = "screen_1"
""")


class ScreenOne(Screen):
   def press_read(self):
      self.ids.lbl1.text = "SharedVar is " + str(GlobalShared.MY_NUMBER)

   def press_change(self):
      GlobalShared.MY_NUMBER = GlobalShared.MY_NUMBER + 1
      self.ids.lbl1.text = "SharedVar is now " + str(GlobalShared.MY_NUMBER)


class ScreenTwo(Screen):
   def press_read(self):
      self.ids.lbl2.text = "SharedVar is now " + str(GlobalShared.MY_NUMBER)

   def press_change(self):
      GlobalShared.MY_NUMBER = GlobalShared.MY_NUMBER + 1
      self.ids.lbl2.text = "SharedVar is " + str(GlobalShared.MY_NUMBER)


class ScreenApp(App):
   sm = ScreenManager()

   def build(self):
      ScreenApp.sm.add_widget(ScreenOne(name='screen_1'))
      ScreenApp.sm.add_widget(ScreenTwo(name='screen_2'))
      return ScreenApp.sm


if __name__ == '__main__':
   ScreenApp().run()