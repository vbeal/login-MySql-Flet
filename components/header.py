import flet as ft

def create_header(show_register_page, show_login_page, switch_theme, appbar_style):
    theme_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Dark", on_click=switch_theme),
            ft.PopupMenuItem(text="Light", on_click=switch_theme),
            ft.PopupMenuItem(text="System", on_click=switch_theme)
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
           # alignment=ft.alignment.center,
        ),
        actions=[
            ft.TextButton(text="Registrar-se", on_click=show_register_page),
            ft.TextButton(text="Login", on_click=show_login_page),
            theme_menu
        ],
        **appbar_style  # Usa os estilos definidos no styles.py
    )
