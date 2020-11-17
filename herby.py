
from kivy import Config

Config.set('graphics', 'multisamples', '0')
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.uix.list import OneLineIconListItem
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.app import MDApp

KV = '''
FloatLayout:
    orientation:"vertical"
    
    ScrollView:
        MDList:
            size_hint_y: None
            height: self.minimum_height
            adaptive_height: True
            padding: dp(10), dp(10)
            spacing: dp(4)
            MDLabel:
                text:"Admin signup!"
                halign:"center"
                pos_hint:{"center_x":.5, "center_y":.95}
            MDIcon:
                icon:"account"
                pos_hint:{"center_x":.75, "center_y":.95}
                color:app.theme_cls.primary_color
            MDTextField:
                id:user_name
                pos_hint:{"center_x":.5, "center_y":.85}
                size_hint:.9, None
                hint_text:"Name:"
                required:True
                helper_text_mode: "on_focus"
                helper_text: "Example: John peter mbuya"
            MDTextField:
                id:user_phone
                pos_hint:{"center_x":.5, "center_y":.75}
                size_hint:.9, None
                hint_text:"Phone Number:"
                required:True
            MDTextField:
                id:user_password
                pos_hint:{"center_x":.5, "center_y":.65}
                size_hint:.9, None
                hint_text:"Password:"
                password:True
                required:True
            MDTextField:
                id:user_city
                pos_hint:{"center_x":.5, "center_y":.55}
                size_hint:.9, None
                hint_text:"City:"
                required:True
            MDTextField:
                id:user_address
                pos_hint:{"center_x":.5, "center_y":.45}
                size_hint:.9, None
                hint_text:"Address:"
                required:True
                helper_text_mode: "on_focus"
                helper_text: "Example: Arusha/sombetini"
            MDTextField:
                id:user_email
                pos_hint:{"center_x":.5, "center_y":.35}
                size_hint:.9, None
                hint_text:"Email:"
                required:True
                helper_text_mode: "on_focus"
                helper_text: "Example: yourname@gmail.com"
            MDLabel
                text:"Company"
                pos_hint: {'center_x': .9, 'center_y': .2}
            Check:
                active: True
                pos_hint: {'center_x': .4, 'center_y': .2}
                on_active: app.type_active(*args)
            MDLabel:
                text:"individual"
                pos_hint: {'center_x': .9, 'center_y': .15}
            Check:
                id:individual
                pos_hint: {'center_x': .6, 'center_y': .5}
            MDFillRoundFlatButton:
                id:register
                text:"Register"
                size_hint: .7, .06
                pos_hint:{"center_x":.5, "center_y":.2}
                text_color:1, 1, 1, 1

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
        
        
        
        


'''

class TestNavigationDrawer(MDApp):
    size_x = NumericProperty(0)
    size_y = NumericProperty(0)
    type_b = StringProperty("")
    
    def type_active(self, checkbox, value):
        if value:
            #print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
            self.type_b = "company"
            print(self.type_b)
        else:
            #print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
            self.type_b = "individual"
            #self.root.ids.individual.active = True
            print(self.type_b)


    def build(self):
        self.size_x, self.size_y = Window.size = (411, 823)
        return Builder.load_string(KV)


TestNavigationDrawer().run()

