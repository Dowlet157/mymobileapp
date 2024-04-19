from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class mdapp(MDApp):
    def build(self):
        return MDLabel(text="Hello! It's me! Mario!!", halign="center")

mdapp().run()
