from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Campo de entrada para o usuário
        self.usuario_input = TextInput(hint_text='Usuário',  size_hint_y=None, height=40, pos_hint={'center_x':0.5, 'center_y':0.5})
        self.add_widget(self.usuario_input)

        # Campo de entrada para a senha
        self.senha_input = TextInput(hint_text='Senha', size_hint_y=None, height=40, password=True)
        self.add_widget(self.senha_input)

        # Botão para realizar o login
        self.login_button = Button(text='Login', size_hint_y=None, height=40)

        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        # Implementar a lógica de login aqui
        usuario = self.usuario_input.text
        senha = self.senha_input.text
        print(f'Usuário: {usuario}, Senha: {senha}')

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()