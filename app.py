# app.py

import flet as ft
from theme import load_theme, save_theme, apply_styles
from pages.login import show_login_page
from pages.register import show_register_page

def navigate_to(page, route, switch_theme):
    if route == "/register":
        page.route = "/register"
        show_register_page(page, switch_theme, navigate_to)
    else:
        page.route = "/login"
        show_login_page(page, switch_theme, navigate_to)

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
        apply_styles(page, switch_theme)
        navigate_to(page, page.route, switch_theme)

    page.switch_theme = switch_theme
    page.navigate_to = navigate_to

    page.route = "/login"
    apply_styles(page, switch_theme)
    navigate_to(page, page.route, switch_theme)

ft.app(target=main)
