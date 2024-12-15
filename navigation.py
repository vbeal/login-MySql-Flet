# navigation.py

from pages.login import show_login_page
from pages.register import show_register_page

def navigate_to(page, route, switch_theme):
    if route == "/register":
        page.route = "/register"
        show_register_page(page, switch_theme)
    else:
        page.route = "/login"
        show_login_page(page, switch_theme)
