import flet as ft

def app_style():
    return {
        "appbar": {
            "bgcolor": ft.colors.BLUE,
            "center_title": False
        },
        "footer": {
            "bgcolor": ft.colors.BLUE_100,
            "padding": 10,
            "alignment": ft.alignment.center
        },
        "text": {
            "size": 24,
            "color": ft.colors.BLACK
        }
    }
