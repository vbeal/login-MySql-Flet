# pages/login.py

import flet as ft
from models import session, Usuario
from utils.security import verify_password
from utils.messages import show_message

def login_page(page, on_login):
    def login(e):
        username = username_field.value
        password = password_field.value
        user = session.query(Usuario).filter(Usuario.username == username).first()
        if user and verify_password(password, user.password):
            show_message(page, "Usuário logado com sucesso!", ft.colors.GREEN)
            print("Usuário logado com sucesso!")
            on_login()
        else:
            show_message(page, "Usuário ou senha incorretos!", ft.colors.RED)
            print("Usuário ou senha incorretos!")

    username_field = ft.TextField(label="Usuário", autofocus=True)
    password_field = ft.TextField(label="Senha", password=True)
    page.add(
        username_field,
        password_field,
        ft.ElevatedButton(text="Login", on_click=login),
        ft.TextButton(text="Registrar-se", on_click=on_login)
    )
