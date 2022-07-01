from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from matplotlib.pyplot import title

class ConverterApp(MDApp):

    def flip(self):
        print("Hello World")


    def build(self):
        screen = MDScreen()
        

        # Add top banner
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        # Add icon to banner and add a function
        # https://kivymd.readthedocs.io/en/latest/themes/icon-definitions/index.html
        self.toolbar.right_action_items = [
            ["rotate-3d", lambda x: self.flip()]]
            

        screen.add_widget(self.toolbar)


        return screen

if __name__ == '__main__':
    ConverterApp().run()