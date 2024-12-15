# components/footer.py

import flet as ft

def create_footer(footer_style):
    return ft.Container(
        content=ft.Text("© 2024 Meu Aplicativo. Todos os direitos reservados.", size=14),
        **footer_style
    )
