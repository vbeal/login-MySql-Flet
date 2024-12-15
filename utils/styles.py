# utils/styles.py

import flet as ft

def app_style(theme_mode):
    if theme_mode == ft.ThemeMode.DARK:
        appbar_color = ft.colors.BLACK
        text_color = ft.colors.WHITE
        button_color = ft.colors.GREY_800
        button_text_color = ft.colors.WHITE
    elif theme_mode == ft.ThemeMode.LIGHT:
        appbar_color = ft.colors.BLUE
        text_color = ft.colors.BLACK
        button_color = ft.colors.LIGHT_BLUE
        button_text_color = ft.colors.BLACK
    else:  # System theme with more vibrant colors
        appbar_color = ft.colors.GREEN
        text_color = ft.colors.PINK
        button_color = ft.colors.RED
        button_text_color = ft.colors.WHITE

    return {
        "appbar": {
            "bgcolor": appbar_color,
            "center_title": False
        },
        "text": {
            "size": 24,
            "color": text_color
        },
        "button": {
            "bgcolor": button_color,
            "color": button_text_color
        }
    }
