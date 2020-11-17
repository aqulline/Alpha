from kivy import Config

Config.set('graphics', 'multisamples', '0')
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.list import MDList, IconLeftWidget, OneLineIconListItem, ILeftBody
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton
from kivymd.theming import ThemableBehavior
from kivymd.icon_definitions import md_icons

class Lists(OneLineIconListItem):
    icon = ObjectProperty()
    

    
    class Icons(IconLeftWidget):
        pass

class main(MDApp):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                print("hello")
                break
        instance_item.text_color = self.theme_cls.primary_color
    def change(self):
        sm = self.root
        sm.current = "two"
    def build(self):
        self.title = "Test"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.accent = "Brown"
        Window.size = (411, 823)


if __name__ == "__main__":
    main().run()
