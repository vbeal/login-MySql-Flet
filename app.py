# app.py

import flet as ft
import bcrypt  # Importar bcrypt para verificar senha hash
from models import Usuario, session

def main(page: ft.Page):
    page.title = "Login Flet"

    # Função para redirecionar o usuário para a página principal
    def redirect_to_main_page():
        page.clean()
        page.title = "Página Principal"
        welcome_text = ft.Text(value="Bem-vindo à Página Principal!", size=24)
        logout_button = ft.ElevatedButton(
            text="Logout", 
            on_click=lambda e: logout()
        )
        page.add(welcome_text, logout_button)

    # Função de login
    def login(e):
        username_input = username.value
        password_input = password.value

        # Verificar se o usuário existe no banco de dados
        user = session.query(Usuario).filter_by(username=username_input).first()
        
        if user and bcrypt.checkpw(password_input.encode('utf-8'), user.password.encode('utf-8')):
            login_message.value = "Login bem-sucedido!"
            login_message.color = ft.colors.GREEN
            login_message.update()
            redirect_to_main_page()
        else:
            login_message.value = "Login falhou. Tente novamente."
            login_message.color = ft.colors.RED
            login_message.update()

    # Função de logout
    def logout():
        page.clean()
        main(page)

    # Campos de entrada e botão de login
    username = ft.TextField(label="Usuário", autofocus=True)
    password = ft.TextField(label="Senha", password=True)
    login_button = ft.ElevatedButton(text="Login", on_click=login)
    login_message = ft.Text()

    # Adicionar componentes à página
    page.add(
        username,
        password,
        login_button,
        login_message
    )

ft.app(target=main)
