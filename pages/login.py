# pages/login.py

import flet as ft
import bcrypt
from models import Usuario, session
from utils.messages import show_message

def login_page(page, redirect_to_main_page, show_register_page):
    # Função de login
    def login(e):
        username_input = login_username.value
        password_input = login_password.value

        # Validação de entrada
        if not username_input or not password_input:
            show_message(page, "Por favor, preencha todos os campos.", ft.colors.RED)
            return

        # Verificar se o usuário existe no banco de dados
        user = session.query(Usuario).filter_by(username=username_input).first()

        if user and bcrypt.checkpw(password_input.encode('utf-8'), user.password.encode('utf-8')):
            show_message(page, "Login bem-sucedido!", ft.colors.GREEN)
            redirect_to_main_page()
        else:
            show_message(page, "Login falhou. Tente novamente.", ft.colors.RED)

    # Campos de entrada e botão de login
    login_username = ft.TextField(label="Usuário", autofocus=True)
    login_password = ft.TextField(label="Senha", password=True)
    login_button = ft.ElevatedButton(text="Login", on_click=login)

    # Adicionar componentes à página
    page.clean()
    page.add(
        ft.Text("Login", size=24, weight=ft.FontWeight.BOLD),
        login_username,
        login_password,
        login_button,
        ft.TextButton(text="Registrar", on_click=show_register_page)
    )
    page.update()
