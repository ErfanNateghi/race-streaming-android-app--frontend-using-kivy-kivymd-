from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.videoplayer import VideoPlayer





class LoginScreen(MDScreen):
    def do_login(self, username, password):
        if username == 'admin' and password == 'admin':
            self.manager.current = 'main_screen'
        else:
            print('Invalid credentials')


class MainScreen(MDScreen):
    def mainpage_to_streampage(self, item_text):
        self.manager.current = item_text

class Box(MDBoxLayout):
    pass

class BaseScreen(MDScreen):
    image_size = StringProperty()

class MainpageCard(MDCard):
    pass

class StreamPage(MDScreen):
    pass

class StreamPageCard(MDCard):
    pass

class StreamPageTopAppBar(MDTopAppBar):
    pass

class F1TeamDetailsScreen(MDScreen):
    pass

class Team_f1_1_screen (MDScreen):
    pass

class F1MDLabel(MDLabel):
    pass

class F1DriversScreen(MDScreen):
    pass

class F1TrackDetailsScreen(MDScreen):
    pass

class Wrc_screen(MDScreen):
    pass

class Wrc_drivers(MDScreen):
    pass

class Wrc_manufacturers(MDScreen):
    pass

class Wrc_trackdetails(MDScreen):
    pass

class Wrc_stages(MDScreen):
    pass

class Wrc_stage_1(MDScreen):
    pass

class Dakar_screen(MDScreen):
    pass

class Wec_screen(MDScreen):
    pass

class Demo_screen(MDScreen):
    pass

# class MyVideoPlayer(VideoPlayer):
#     show_controls = BooleanProperty(True)
#     controls_widget = ObjectProperty(None, allownone = True)

#     def __init__(self, **kw):
#         super().__init__(**kw)

#         self.bind(parent = self.get_controls)

#     def get_controls(self, inst, controls, *_):
#         if len(self.children):
#             self.controls_widget = self.children[0]
#             self.unbind(parent = self.get_controls)

#     def on_controls_widget(self, inst, controls):
#         self.add_or_remove_controls(self.show_controls)


#     def add_or_remove_controls(self, is_show):
#         controls = self.controls_widget
#         if not controls: return

#         if not is_show and controls in self.children:
#             self.remove_widget(controls)
#         elif is_show and not controls in self.children:
#             self.add_widget(controls)


#     def on_show_controls(self, inst, is_show):
#         self.add_or_remove_controls(is_show)