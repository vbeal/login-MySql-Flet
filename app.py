# app.py

import flet as ft
import json
import os
from components.header import create_header
from utils.styles import app_style
from models import session, Usuario
from register_user import cadastrar_usuario
from utils.security import verify_password
from utils.messages import show_message

def load_theme():
    if os.path.exists("theme.json"):
        try:
            with open("theme.json", "r") as file:
                data = json.load(file)
                print(f"Loaded theme: {data}")
                theme = data.get("theme", "LIGHT")
                if theme == "DARK":
                    return ft.ThemeMode.DARK
                elif theme == "LIGHT":
                    return ft.ThemeMode.LIGHT
                else:
                    return ft.ThemeMode.SYSTEM
        except (json.JSONDecodeError, ValueError):
            return ft.ThemeMode.LIGHT
    return ft.ThemeMode.LIGHT

def save_theme(theme):
    theme_str = "LIGHT"
    if theme == ft.ThemeMode.DARK:
        theme_str = "DARK"
    elif theme == ft.ThemeMode.LIGHT:
        theme_str = "LIGHT"
    else:
        theme_str = "SYSTEM"
    with open("theme.json", "w") as file:
        json.dump({"theme": theme_str}, file)
    print(f"Saved theme: {theme_str}")

def main(page: ft.Page):
    page.title = "Flet App - Tema"
    page.theme_mode = load_theme()
    print(f"Initial theme mode: {page.theme_mode}")

    def switch_theme(e):
        theme_map = {
            "Dark": ft.ThemeMode.DARK,
            "Light": ft.ThemeMode.LIGHT,
            "System": ft.ThemeMode.SYSTEM
        }
        new_theme = theme_map.get(e.control.text, ft.ThemeMode.LIGHT)
        print(f"Switching to theme: {e.control.text}, Mapped theme: {new_theme}")
        page.theme_mode = new_theme
        save_theme(new_theme)
        page.update()
        apply_styles()

    def apply_styles():
        styles = app_style(page.theme_mode)
        print(f"Applied styles: {styles}")
        page.controls.clear()
        page.appbar = create_header(page, switch_theme, styles["appbar"])
        if page.route == "/login":
            show_login_page()
        elif page.route == "/register":
            show_register_page()
        page.update()

    def redirect_to_main_page():
        styles = app_style(page.theme_mode)
        page.controls.clear()
        page.appbar = create_header(page, switch_theme, styles["appbar"])
        page.add(
            ft.Text(value="Bem-vindo à Página Principal!", size=24, style=styles["text"]),
            ft.ElevatedButton(
                text="Logout",
                on_click=show_login_page,
                bgcolor=styles["button"]["bgcolor"],
                color=styles["button"]["color"]
            )
        )
        page.update()

    def show_login_page(e=None):
        page.route = "/login"
        styles = app_style(page.theme_mode)
        page.appbar = create_header(page, switch_theme, styles["appbar"])
        page.controls.clear()

        def login(e):
            username = username_field.value
            password = password_field.value
            user = session.query(Usuario).filter(Usuario.username == username).first()
            if user and verify_password(password, user.password):
                show_message(page, "Usuário logado com sucesso!", ft.colors.GREEN)
                print("Usuário logado com sucesso!")
                redirect_to_main_page()
            else:
                show_message(page, "Usuário ou senha incorretos!", ft.colors.RED)
                print("Usuário ou senha incorretos!")

        def on_register_page(e):
            show_register_page()

        username_field = ft.TextField(label="Usuário", autofocus=True)
        password_field = ft.TextField(label="Senha", password=True)
        page.add(
            username_field,
            password_field,
            ft.ElevatedButton(text="Login", on_click=login),
            ft.TextButton(text="Registrar-se", on_click=on_register_page)
        )
        page.update()

    def show_register_page(e=None):
        page.route = "/register"
        styles = app_style(page.theme_mode)
        page.appbar = create_header(page, switch_theme, styles["appbar"])
        page.controls.clear()

        def register(e):
            username = username_field.value
            password = password_field.value
            try:
                cadastrar_usuario(username, password)
                show_message(page, "Usuário registrado com sucesso!", ft.colors.GREEN)
                print("Usuário registrado com sucesso!")
                show_login_page()
            except Exception as ex:
                show_message(page, f"Erro ao registrar usuário: {ex}", ft.colors.RED)
                print(f"Erro ao registrar usuário: {ex}")

        def on_login_page(e):
            show_login_page()

        username_field = ft.TextField(label="Usuário", autofocus=True)
        password_field = ft.TextField(label="Senha", password=True)
        page.add(
            username_field,
            password_field,
            ft.ElevatedButton(text="Registrar-se", on_click=register),
            ft.TextButton(text="Login", on_click=on_login_page)
        )
        page.update()

    show_login_page()

ft.app(target=main)
