# pages/register.py

import flet as ft
from register_user import cadastrar_usuario
from utils.messages import show_message
from models import session, Usuario

def show_register_page(page, switch_theme, navigate_to):
    def register(e):
        username = username_field.value
        password = password_field.value

        # Verificar se o nome de usuário já existe
        existing_user = session.query(Usuario).filter(Usuario.username == username).first()
        if existing_user:
            show_message(page, "Nome de usuário já existe. Escolha outro.", ft.colors.RED)
            print("Nome de usuário já existe.")
            return

        try:
            cadastrar_usuario(username, password)
            session.commit()  # Garantir que a sessão seja comprometida
            show_message(page, "Usuário registrado com sucesso!", ft.colors.GREEN)
            print("Usuário registrado com sucesso!")
            navigate_to(page, "/login", switch_theme)
        except Exception as ex:
            session.rollback()  # Fazer rollback da sessão em caso de erro
            show_message(page, f"Erro ao registrar usuário: {ex}", ft.colors.RED)
            print(f"Erro ao registrar usuário: {ex}")

    def on_login_page(e):
        navigate_to(page, "/login", switch_theme)

    page.controls.clear()
    username_field = ft.TextField(label="Usuário", autofocus=True)
    password_field = ft.TextField(label="Senha", password=True)
    page.add(
        username_field,
        password_field,
        ft.ElevatedButton(text="Registrar-se", on_click=register),
        ft.TextButton(text="Login", on_click=on_login_page)
    )
    page.update()
