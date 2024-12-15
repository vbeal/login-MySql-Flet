# app.py

import flet as ft
from pages.login import login_page
from pages.register import register_page

def main(page: ft.Page):
    page.title = "Flet App - Login e Registro"
    page.theme_mode = ft.ThemeMode.LIGHT  # Define o modo claro

    # Função para redirecionar o usuário para a página principal
    def redirect_to_main_page():
        page.clean()
        page.title = "Página Principal"
        welcome_text = ft.Text(value="Bem-vindo à Página Principal!", size=24)
        logout_button = ft.ElevatedButton(
            text="Logout",
            on_click=lambda e: show_login_page()
        )
        page.add(welcome_text, logout_button)
        page.update()  # Atualiza a página

    # Função para mostrar a página de login
    def show_login_page(e=None):
        login_page(page, redirect_to_main_page, show_register_page)

    # Função para mostrar a página de registro
    def show_register_page(e=None):
        register_page(page, show_login_page)

    # Mostrar a página de login inicialmente
    show_login_page()

ft.app(target=main)
