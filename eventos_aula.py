from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
import re 


class MeuWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MeuWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # on_touch_down, on_touch_move, on_touch_up
        # self.touch_widget = Label()
        # self.touch_widget.bind(on_touch_down=self.on_touch_down)
        # self.touch_widget.bind(on_touch_move=self.on_touch_move)
        # self.touch_widget.bind(on_touch_up=self.on_touch_up)
        # self.add_widget(self.touch_widget)

        # on_enter, on_leave
        self.text_input = TextInput(hint_text='Digite seu nome')
        self.text_input.bind(on_focus=self.on_enter)
        self.text_input.bind(on_unfocus=self.on_leave)
        self.add_widget(self.text_input)

        # on_press, on_release
        self.button = Button(text='Clique aqui')
        self.button.bind(on_press=self.on_press)
        self.button.bind(on_release=self.on_release)
        self.add_widget(self.button)

        # on_text_validate
        self.text_input_validate = TextInput(hint_text='Digite seu email e pressione entre ( se não apertar enter é gay)', multiline=False)
        self.text_input_validate.bind(on_text_validate=self.on_text_validate)
        self.add_widget(self.text_input_validate)



        # on_checkbox_active
        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox)

        # on_slider_value_change
        self.slider = Slider(min=0, max=100, value=50)
        self.slider.bind(value=self.on_slider_value_change)
        self.add_widget(self.slider)

    # def on_touch_down(self, touch, *args):
    #     print('Toque iniciado')
        
    #     if touch.button == 'scrollup' or touch.button == 'scrolldown':
    #         print('O usuário está rolando a tela com o mouse')
    #         return False

    # def on_touch_move(self, touch):
    #     print('Toque movido')
    #     return False

    # def on_touch_up(self, touch):
    #     print('Toque finalizado')
    #     return False

    def on_enter(self, instance):
        print('Foco ganho')

    def on_leave(self, instance):
        print('Foco perdido')

    def on_press(self, instance):
        print('Botão pressionado')

    def on_release(self, instance):
        print('Botão liberado')

    # def on_text_validate(self, instance):
    #     print('Texto validado')
    #     texto = instance.text
    #     if re.match(r"[^@]+@[^@]+\.[^@]+", texto):
    #         popup = Popup(title='E-mail válido', content=Label(text='O e-mail é válido!'), size_hint=(None, None), size=(400, 200))
    #         popup.open()
    #     else:
    #         popup = Popup(title='E-mail inválido', content=Label(text='O e-mail é inválido!'), size_hint=(None, None), size=(400, 200))
    #         popup.open()


    def on_text_validate(self, instance):
        texto = instance.text
        if re.match(r"[^@]+@[^@]+\.[^@]+", texto):
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(Label(text='O e-mail é válido!'))
            layout.add_widget(Button(text='OK', on_press=lambda x: popup.dismiss()))
            popup = Popup(title='E-mail válido', content=layout, size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(Label(text='O e-mail é inválido!'))
            layout.add_widget(Button(text='OK', on_press=lambda x: popup.dismiss()))
            popup = Popup(title='E-mail inválido', content=layout, size_hint=(None, None), size=(400, 200))
            popup.open()

    def on_checkbox_active(self, instance, value):
        if value:
            print('Checkbox checked')
        else:
            print('Checkbox unchecked')

    def on_slider_value_change(self, instance, value):
        print('Valor do slider alterado')

class MeuApp(App):
    def build(self):
        return MeuWidget()

if __name__ == '__main__':
    MeuApp().run()