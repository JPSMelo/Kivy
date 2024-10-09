from kivy.app import App  
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

#ctrl+k e depois ctrl +C

class Floatex(App):
    def build(self):
        layout = FloatLayout()
        layout.add_widget(Button(text='botao1',pos_hint={'center_x':0.5, 'center_y':0.5}, size_hint =(0.5, 0.2),font_size=50))
        layout.add_widget(Label(text='oi',font_size=90))
        # layout.add_widget(Button(text='botao1', pos=(x, y)))
        return layout
    
if __name__ =='__main__':
    Floatex().run()

