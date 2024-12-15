# app.py

import flet as ft
from components.header import create_header
from components.footer import create_footer
from pages.login import login_page
from pages.register import register_page
from utils.styles import app_style

def main(page: ft.Page):
    page.title = "Flet App - Login e Registro"
    page.theme_mode = ft.ThemeMode.LIGHT  # Define o modo claro inicialmente

    styles = app_style()

    # Função para alternar tema
    def switch_theme(e):
        if e.control.text == "Dark":
            page.theme_mode = ft.ThemeMode.DARK
        elif e.control.text == "Light":
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.SYSTEM
        page.update()

    # Função para redirecionar o usuário para a página principal
    def redirect_to_main_page():
        page.clean()
        page.appbar = create_header(show_register_page, show_login_page, switch_theme, styles["appbar"])
        page.add(
            ft.Text(value="Bem-vindo à Página Principal!", size=24, style=styles["text"]),
            ft.ElevatedButton(
                text="Logout",
                on_click=lambda e: show_login_page()
            )
        )
        page.add(create_footer(styles["footer"]))
        page.update()  # Atualiza a página

    # Função para mostrar a página de login
    def show_login_page(e=None):
        page.clean()
        page.appbar = create_header(show_register_page, show_login_page, switch_theme, styles["appbar"])
        login_page(page, redirect_to_main_page, show_register_page)
        page.add(create_footer(styles["footer"]))
        page.update()

    # Função para mostrar a página de registro
    def show_register_page(e=None):
        page.clean()
        page.appbar = create_header(show_register_page, show_login_page, switch_theme, styles["appbar"])
        register_page(page, show_login_page)
        page.add(create_footer(styles["footer"]))
        page.update()

    # Mostrar a página de login inicialmente
    show_login_page()

ft.app(target=main)
