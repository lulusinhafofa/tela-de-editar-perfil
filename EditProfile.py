from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.core.window import Window

Window.size = (400, 620)

class RoundedButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (1, 0.5, 0.5, 1) 

        with self.canvas.before:
            Color(1, 0.5, 0.5, 1)  
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[30])

        self.bind(size=self.update_background, pos=self.update_background)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def on_press(self):
        print(f"{self.text} pressionado")

    def on_release(self):
        print(f"{self.text} solto")


class TextInputWithSquareBackground(TextInput):
    def __init__(self, **kwargs):
        super(TextInputWithSquareBackground, self).__init__(**kwargs)
        self.background_color = (1, 1, 1, 1)  

        with self.canvas.before:
            Color(1, 0.5, 0.6, 1)  
            self.background = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])

        self.bind(size=self.update_background, pos=self.update_background)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def on_text_validate(self):
        print(f"Texto validado: {self.text}")

    def on_focus(self, instance, value):
        if not value:  
            print(f"Caixa de entrada perdeu o foco. Texto: {self.text}")


class EditProfileScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(EditProfileScreen, self).__init__(**kwargs)
        self.create_background()
        self.add_circle()
        self.add_profile_image()
        self.add_buttons()
        self.add_text_inputs()

    def create_background(self):
        with self.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = RoundedRectangle(size=Window.size, pos=self.pos, radius=[0])

    def add_circle(self):
        with self.canvas.before:
            Color(1, 0.5, 0.5, 1)  
            self.circle = Ellipse(size=(165, 165), pos=(Window.width / 2 - 83, Window.height * 0.9 - 182))

    def add_profile_image(self):
        self.profile_image = Image(source="C:\\Users\\lulusinha\\Downloads\\3736502.png", size_hint=(None, None), size=(150, 150),
                                   pos=(Window.width / 2 - 75, Window.height * 0.9 - 175))
        self.add_widget(self.profile_image)

    def add_buttons(self):
        self.add_edit_photo_button()
        self.add_save_changes_button()

    def add_edit_photo_button(self):
        self.edit_photo_button = RoundedButton(text="Editar Foto de Perfil", size_hint=(None, None), size=(150, 50),
                                               pos_hint={'center_x': 0.6, 'top': 0.7}) 
        self.add_widget(self.edit_photo_button)

    def add_save_changes_button(self):
        self.save_changes_button = RoundedButton(text="Salvar Alterações", size_hint=(None, None), size=(200, 55),
                                                 pos_hint={'center_x': 0.5, 'y': 0.02})  
        self.add_widget(self.save_changes_button)

    def add_text_inputs(self):
        self.add_name_input()
        self.add_email_input()
        self.add_story_input()

    def add_name_input(self):
        self.name_input = TextInput(hint_text="Nome", size_hint=(None, None), size=(300, 65),
                                                        pos_hint={'center_x': 0.5, 'y': 0.45})  
        self.add_widget(self.name_input)

    def add_email_input(self):
        self.email_input = TextInput(hint_text="Email", size_hint=(None, None), size=(300, 65),
                                                         pos_hint={'center_x': 0.5, 'y': 0.3}) 
        self.add_widget(self.email_input)

    def add_story_input(self):
        self.story_input = TextInput(hint_text="História", size_hint=(None, None), size=(300, 65),
                                                          pos_hint={'center_x': 0.5, 'y': 0.15})  
        self.add_widget(self.story_input)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class TestApp(App):
    def build(self):
        return EditProfileScreen()


if __name__ == '__main__':
    TestApp().run()

