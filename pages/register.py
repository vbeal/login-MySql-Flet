# pages/register.py

import flet as ft
from models import Usuario, session
from register_user import cadastrar_usuario
from utils.messages import show_message

def register_page(page, show_login_page):
    # Função de registro
    def register(e):
        username_input = register_username.value
        password_input = register_password.value

        # Validação de entrada
        if not username_input or not password_input:
            show_message(page, "Por favor, preencha todos os campos.", ft.colors.RED)
            return

        # Verificar se o usuário já existe no banco de dados
        if session.query(Usuario).filter_by(username=username_input).first():
            show_message(page, "Nome de usuário já existe.", ft.colors.RED)
            return

        # Cadastrar novo usuário
        cadastrar_usuario(username_input, password_input)
        show_message(page, "Usuário registrado com sucesso!", ft.colors.GREEN)
        show_login_page(e)

    # Campos de entrada e botão de registro
    register_username = ft.TextField(label="Novo Usuário", autofocus=True)
    register_password = ft.TextField(label="Nova Senha", password=True)
    register_button = ft.ElevatedButton(text="Registrar", on_click=register)

    # Adicionar componentes à página
    page.clean()
    page.add(
        ft.Text("Registrar", size=24, weight=ft.FontWeight.BOLD),
        register_username,
        register_password,
        register_button,
        ft.TextButton(text="Voltar para Login", on_click=show_login_page)
    )
    page.update()
