#!/usr/bin/env python3
"""This is just a very simple authentication example.

Please see the `OAuth2 example at FastAPI <https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/>`_  or
use the great `Authlib package <https://docs.authlib.org/en/v0.13/client/starlette.html#using-fastapi>`_ to implement a classing real authentication system.
Here we just demonstrate the NiceGUI integration.
"""
import sys
import time

from PyQt5.QtWidgets import QApplication
from fastapi.responses import RedirectResponse

import subprocess
from main import main

from nicegui import app, ui
from starlette.responses import RedirectResponse

from GUI.gui import MainWindow

# in reality users passwords would obviously need to be hashed
passwords = {'Tim': 'Caus', 'Bruno': 'Zen'}


@ui.page('/')
def main_page() -> RedirectResponse:
    if not app.storage.user.get('authenticated', False):
        return RedirectResponse('/login')
    with ui.column().classes('absolute-center items-center'):
        ui.button(on_click=lambda: (app.storage.user.clear(), ui.open('/login')), icon='logout').props('outline round')


@ui.page('/login')
def login() -> RedirectResponse:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            main()

        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)


ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')
