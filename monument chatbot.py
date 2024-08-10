# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:45:37 2024

@author: harsh
"""

from kivymd.app import MDApp
from kivy.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="welcome to this world, Baby", halign="center")

if __name__=='__main__':
    Main_App().run()