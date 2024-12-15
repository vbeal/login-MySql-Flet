# pages/login.py

import flet as ft
from models import session, Usuario
from utils.security import verify_password
from utils.messages import show_message
from utils.styles import app_style  # Importar app_style
from components.header import create_header  # Importar create_header

def show_login_page(page, switch_theme, navigate_to):
    def login(e):
        username = username_field.value
        password = password_field.value
        user = session.query(Usuario).filter(Usuario.username == username).first()
        if user and verify_password(password, user.password):
            show_message(page, "Usuário logado com sucesso!", ft.colors.GREEN)
            print("Usuário logado com sucesso!")
            redirect_to_main_page(page, switch_theme, navigate_to)
        else:
            show_message(page, "Usuário ou senha incorretos!", ft.colors.RED)
            print("Usuário ou senha incorretos!")

    def on_register_page(e):
        navigate_to(page, "/register", switch_theme)

    page.controls.clear()
    username_field = ft.TextField(label="Usuário", autofocus=True)
    password_field = ft.TextField(label="Senha", password=True)
    page.add(
        username_field,
        password_field,
        ft.ElevatedButton(text="Login", on_click=login),
        ft.TextButton(text="Registrar-se", on_click=on_register_page)
    )
    page.update()

def redirect_to_main_page(page, switch_theme, navigate_to):
    styles = app_style(page.theme_mode)
    page.controls.clear()
    page.appbar = create_header(page, switch_theme, styles["appbar"])
    page.add(
        ft.Text(value="Bem-vindo à Página Principal!", size=24, style=styles["text"]),
        ft.ElevatedButton(
            text="Logout",
            on_click=lambda e: navigate_to(page, "/login", switch_theme),
            bgcolor=styles["button"]["bgcolor"],
            color=styles["button"]["color"]
        )
    )
    page.update()
