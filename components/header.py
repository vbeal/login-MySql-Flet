# components/header.py

import flet as ft

def create_header(show_register_page, show_login_page, switch_theme):
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
