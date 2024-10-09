from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput

class MeuWidget(Label):
    def __init__(self, **kwargs):
        super(MeuWidget, self).__init__(**kwargs)
        self.text = 'Olá, bando de fi de cruscredo'

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        text_input = TextInput(hint_text='Digite seu nome')
        checkbox = CheckBox()
        image = Image(source='imagem.jpg')
        spinner = Spinner(text='Selecione uma opção', values=['Opção 1', 'Opção 2', 'Opção 3'])

        layout.add_widget(text_input)
        layout.add_widget(checkbox)
        self.slider = Slider(min=0, max=100000, value=50000)
        self.label = Label(text='Valor do slider: 50')
        layout.add_widget(self.slider)
        layout.add_widget(self.label)

        self.slider.bind(value=self.on_slider_value_change)


        layout.add_widget(image)
        layout.add_widget(spinner)

        return layout

    def on_slider_value_change(self, instance, value):
            self.label.text = f'Valor do slider: {int(value)}'

if __name__ == '__main__':
    MeuApp().run()