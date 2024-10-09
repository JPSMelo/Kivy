from kivy.app import App  
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

class RelativeLayoutEx(App):
    def build(self):
        layout =RelativeLayout()
        #layout.add_widget(Label(text='Cala boca lucas :)', center_x=0.5, center_y=0.5))
        btn = ToggleButton(text='no projeto da aula passada, coloquem cores nos botões e relativizem sua posição. '
                           , right=100, top=100, font_size=25)
        btn.background_color =(1,0,0,1) 
        layout.add_widget(btn)
        return layout

# def changecolor():
#     togg

if __name__ =='__main__':
    RelativeLayoutEx().run()
