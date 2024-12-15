# components/footer.py

import flet as ft

def create_footer():
    return ft.Container(
        content=ft.Text("© 2024 Meu Aplicativo. Todos os direitos reservados.", size=14),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_100,
        padding=10
    )
