# utils/messages.py

import flet as ft
import threading
from time import sleep

def show_message(page, text, color):
    # Remover qualquer mensagem existente
    if len(page.controls) > 1 and isinstance(page.controls[-1], ft.Container):
        page.controls.pop()
    
    message_container = ft.Container(
        content=ft.Row(
            [
                ft.Icon(
                    ft.icons.ERROR if color == ft.colors.RED else ft.icons.CHECK_CIRCLE,
                    color=color,
                    size=24,
                ),
                ft.Text(text, color=color, size=16)  # Garantir que o texto é adicionado corretamente
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=10,
        margin=10,
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        border=ft.border.all(color=color, width=1),  # Adicionando borda colorida
    )
    
    page.controls.append(message_container)
    page.update()

    def hide_message():
        sleep(3)
        if message_container in page.controls:
            page.controls.remove(message_container)
            page.update()

    threading.Thread(target=hide_message).start()
