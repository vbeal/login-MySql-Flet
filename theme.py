# theme.py

import json
import os
import flet as ft
from components.header import create_header
from utils.styles import app_style

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

def apply_styles(page, switch_theme):
    styles = app_style(page.theme_mode)
    print(f"Applied styles: {styles}")
    page.controls.clear()
    page.appbar = create_header(page, switch_theme, styles["appbar"])
    page.update()
