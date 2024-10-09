from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


class BoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Comi o cu de quem tá lendo (menos patricia pq ela é gente boa)'))
        layout.add_widget(Button(text='Aperte'))
        layout.add_widget(ProgressBar(max=100 ,value =50))
        return layout


if __name__ =='__main__':
    BoxLayoutExample().run()

