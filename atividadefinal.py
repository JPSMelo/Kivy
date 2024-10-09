from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.email_input = TextInput(hint_text='Email', pos_hint={'center_x':0.5, 'center_y':0.5}, size_hint =(0.5, 0.2))
        self.password_input = TextInput(hint_text='Password', password=True, pos_hint={'center_x':0.5, 'center_y':0.5}, size_hint =(0.5, 0.2))
        self.login_button = Button(text='Login',pos_hint={'center_x':0.5, 'center_y':0.5}, size_hint =(0.5, 0.2))

        self.add_widget(self.email_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

        self.login_button.bind(on_press=self.login)

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        # Verify email format using a simple regular expression
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(email_regex, email):
            # Verify login credentials here
            if email == 'atividade@exemple.com' and password == 'joao':
                print('Login bem-sucedido!')
            else:
                print('Credenciais inválidas!')
        else:
            print('Email inválido!')

class Login_no_App_do_JoãoApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    Login_no_App_do_JoãoApp().run()