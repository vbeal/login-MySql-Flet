# components/header.py

import flet as ft

def create_header(page, switch_theme, appbar_style):
    def theme_menu():
        return ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="Dark",
                    on_click=switch_theme,
                    icon=ft.Icons.CHECK if page.theme_mode == ft.ThemeMode.DARK else None
                ),
                ft.PopupMenuItem(
                    text="Light",
                    on_click=switch_theme,
                    icon=ft.Icons.CHECK if page.theme_mode == ft.ThemeMode.LIGHT else None
                ),
                ft.PopupMenuItem(
                    text="System",
                    on_click=switch_theme,
                    icon=ft.Icons.CHECK if page.theme_mode == ft.ThemeMode.SYSTEM else None
                ),
            ]
        )

    return ft.AppBar(
        title=ft.Container(
            content=ft.Image(
                src="assets/logo.png",
                width=165,  # Largura fixa
                height=30,  # Altura fixa
                fit=ft.ImageFit.CONTAIN
            ),
        ),
        actions=[
            theme_menu()
        ],
        **appbar_style  # Usa os estilos definidos no styles.py
    )
