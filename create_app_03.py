from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from matplotlib import image
from matplotlib.pyplot import title
from sympy import source

class ConverterApp(MDApp):

    def flip(self):
        print("Hello World")


    def build(self):
        screen = MDScreen()
        

        # Add top banner
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        # Add icon to banner and add a function def flip(self)
        # https://kivymd.readthedocs.io/en/latest/themes/icon-definitions/index.html
        self.toolbar.right_action_items = [
            ["rotate-3d", lambda x: self.flip()]]

        #################################################
                     
        # display to top banner to app (self.toolbar)
        screen.add_widget(self.toolbar)

        # Add Logo
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"centre_x": 0.5, "centre_y": 0.7}
        ))

        #################################################

        # User input
        self.input = MDTextField(
            text="enter a binary number",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 22
        )
        # display to user input to app (self.input)
        screen.add_widget(self.input)

        #################################################

        # Add Label widget secondary and primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        # display to labels to app (self.label) (self.converted)
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        #################################################


        return screen

if __name__ == '__main__':
    ConverterApp().run()