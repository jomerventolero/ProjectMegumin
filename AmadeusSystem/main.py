# Author: Oreki Houtaro
# Gmail: orekihoutaro1218@gmail.com

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas
import os
import sys
import hashlib as hl
import sqlite3 as s


if sys.platform.startswith('win'):
    top_dir = 'C:\\'
else: 
    top_dir = '/storage/sdcard0/'

trace = True  


class AmadeusSystem:
    def __init__(self, **kwargs):
        pass


    def search_file(self, ext_name, root_dir=top_dir):
        allfiles = []
        for dirs, _, files in os.walk(root_dir):
            print(dirs)
            print(files)
            for f in files:
                if f.endswith(ext_name):
                    print(f)
                    fullname = os.path.join(dirs, f)
                    allfiles.append(fullname)
        allfiles.sort()
        return allfiles


class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.cols = 1
        self.margin = 35

        self.bg_img = Image(source = os.getcwd() + "\\KivyProjects\\AmadeusSystem\\images\\AmadeusLogo.png")
        self.add_widget(self.bg_img)

        self.user_label = Label(text="Username: ", size_hint=(0.05,0.05))
        self.pass_label = Label(text="Password: ", size_hint=(0.05,0.05))
        self.username = TextInput(text="",
                                  multiline=False,
                                  x=60,
                                  y=60,
                                  size_hint=(.06,.06))
        self.password = TextInput(text="",
                                  password=True,
                                  multiline=False,
                                  size_hint=(.06,.06))

        self.login_btn = Button(text="L O G I N", 
                                size_hint=(.06,.06))

        self.add_widget(self.user_label)
        self.add_widget(self.username)
        self.add_widget(self.pass_label)
        self.add_widget(self.password)
        self.add_widget(self.login_btn)
        self.login_btn.bind(on_press=self.login(self.username.text,
                                                self.password.text))


    def create_hash(self, msg):
        return hl.sha512(msg).hexdigest()

    # returns True if the user credentials match one in the database.
    def login(self, username, password):
        db = self.connect_database()
        pwd = self.create_hash(password)
        query = '''SELECT 
                    username, password 
                   FROM users
                   WHERE username == \'{}\', 
                   AND password == \'{}\''''.format(username, pwd)
        db.execute(query)
        db.commit()
        
        db.close()


    


    def connect_database(self):
        database = s.connect(os.getcwd + 'users.db')
        return database
        

    def check_hash(self, pwd, hashpwd):
        if pwd == hashpwd:
            return True
        else:
            return False


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

        self.cols = 2
        
        



class AmadeusSystemApp(App):
    def build(self):
        # Instance of the ScreenManager Class
        self.screen_manager = ScreenManager()

        self.login_page = LoginPage()
        screen = Screen("Login")
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        self.screen_manager.current = "Login"
if __name__ == '__main__':
    # Instance of the AmadeusSystemApp Class
    amd = AmadeusSystemApp()
    amd.run()
