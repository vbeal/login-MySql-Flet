# app.py

import flet as ft
from pages.login import login_page
from pages.register import register_page

def main(page: ft.Page):
    page.title = "Flet App - Login e Registro"
    page.theme_mode = ft.ThemeMode.LIGHT  # Define o modo claro inicialmente

    # Função para alternar tema
    def switch_theme(e):
        if e.control.text == "Dark":
            page.theme_mode = ft.ThemeMode.DARK
        elif e.control.text == "Light":
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.SYSTEM
        page.update()

    # Função para criar o cabeçalho
    def create_header():
        theme_menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Dark", on_click=switch_theme),
                ft.PopupMenuItem(text="Light", on_click=switch_theme),
                ft.PopupMenuItem(text="System", on_click=switch_theme)
            ]
        )
        return ft.AppBar(
            leading=ft.Image(src="logo.png", width=50, height=50),
            title=ft.Text(""),
            actions=[
                ft.TextButton(text="Registrar-se", on_click=show_register_page),
                ft.TextButton(text="Login", on_click=show_login_page),
                theme_menu  # Adiciona o menu de tema no cabeçalho
            ],
            center_title=True,
            bgcolor=ft.colors.BLUE
        )
    
    # Função para criar o rodapé
    def create_footer():
        return ft.Container(
            content=ft.Text("© 2024 Meu Aplicativo. Todos os direitos reservados.", size=14),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_100,
            padding=10
        )

    # Função para redirecionar o usuário para a página principal
    def redirect_to_main_page():
        page.clean()
        page.appbar = create_header()
        page.add(
            ft.Text(value="Bem-vindo à Página Principal!", size=24),
            ft.ElevatedButton(
                text="Logout",
                on_click=lambda e: show_login_page()
            )
        )
        page.add(create_footer())
        page.update()  # Atualiza a página

    # Função para mostrar a página de login
    def show_login_page(e=None):
        page.clean()
        page.appbar = create_header()
        login_page(page, redirect_to_main_page, show_register_page)
        page.add(create_footer())
        page.update()

    # Função para mostrar a página de registro
    def show_register_page(e=None):
        page.clean()
        page.appbar = create_header()
        register_page(page, show_login_page)
        page.add(create_footer())
        page.update()

    # Mostrar a página de login inicialmente
    show_login_page()

ft.app(target=main)
