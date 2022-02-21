import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


import random

kivy.require("2.0.0")

service = []
accounts = {}
chars = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV123456789!£$&#"
charsE = "*&^%$£!"



class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()
        

    def generate_password(self):
        text = self.ids.input.text
        password = ""
        for x in range(1,int(text)):


            password_char = random.choice(chars) 
            password = password + password_char
        password = password + random.choice(charsE)
        self.random_label.text = password
        
class PasswordManager(App):
    def build(self):
        ### Returns the UI
        return MyRoot()
    def process(self):
        text = self.root.ids.input.text
        print(text)

passwordManager = PasswordManager()

if __name__ == "__main__":
    passwordManager.run()