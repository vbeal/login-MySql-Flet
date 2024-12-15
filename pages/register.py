# pages/register.py

import flet as ft
from register_user import cadastrar_usuario
from utils.messages import show_message

def register_page(page, on_login):
    def register(e):
        username = username_field.value
        password = password_field.value
        try:
            cadastrar_usuario(username, password)
            show_message(page, "Usuário registrado com sucesso!", ft.colors.GREEN)
            print("Usuário registrado com sucesso!")
            on_login()
        except Exception as ex:
            show_message(page, f"Erro ao registrar usuário: {ex}", ft.colors.RED)
            print(f"Erro ao registrar usuário: {ex}")

    username_field = ft.TextField(label="Usuário", autofocus=True)
    password_field = ft.TextField(label="Senha", password=True)
    page.add(
        username_field,
        password_field,
        ft.ElevatedButton(text="Registrar-se", on_click=register),
        ft.TextButton(text="Login", on_click=on_login)
    )
