from pyautogui import locateOnScreen, click, center
from webbrowser import open
from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'