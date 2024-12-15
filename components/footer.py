# components/footer.py

import flet as ft

def create_footer():
    return ft.Container(
        content=ft.Text("Rodapé do aplicativo"),
        padding=10,
        alignment=ft.alignment.center
    )
