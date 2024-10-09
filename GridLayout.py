from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


class GridLayoutExample(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayoutExample, self).__init__(**kwargs)
        self.cols = 2
        coluna1 = BoxLayout(orientation='vertical', size_hint_x=0.3)
        b1 = Button(text='Aperte')
        b2 = Button(text='Pressione')
        b3 = Button(text='Bota bota')
        coluna1.add_widget(b1)
        coluna1.add_widget(b2)
        coluna1.add_widget(b3)
        self.add_widget(coluna1)

        coluna2 = PageLayout(size_hint_x=0.7)

        page1 = BoxLayout(orientation='vertical')
        page1.add_widget(Button(text='Página 1'))

        page2 = BoxLayout(orientation='vertical')
        page2.add_widget(Button(text='Página 2'))

        page3 = BoxLayout(orientation='vertical')
        page3.add_widget(Button(text='Página 3'))
        page3.add_widget(ProgressBar(max=100 , value=100))

        coluna2.add_widget(page1)
        coluna2.add_widget(page2)
        coluna2.add_widget(page3)
        self.add_widget(coluna2)


        

class MyApp(App):
    def build(self):
        return GridLayoutExample()



if __name__ =='__main__':
    MyApp().run()

