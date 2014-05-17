#!/usr/bin/env python3

import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

class WelcomeScreen(BoxLayout):
    def do_action(self):
        print('foo')

class LabKasseApp(App):
    def build(self):
        return WelcomeScreen()

if __name__ == '__main__':
    LabKasseApp().run()
