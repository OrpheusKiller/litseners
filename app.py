from pyautogui import locateOnScreen, click, center
from webbrowser import open
from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    open("https://www.youtube.com/watch?v=oWsnhdwJ_Vw")

    while True:
        try:
            locateOnScreen("static\\logo.png", confidence=0.9)
            break
        except:
            sleep(5)
            continue

    try:
        if locateOnScreen("static\\subscribe.png", confidence=0.9):
            click(center(locateOnScreen("static\\subscribe.png", confidence=0.9)))
    except:
            pass

    try:
        if locateOnScreen("static\\like.png", confidence=0.9):
            click(center(locateOnScreen("static\\like.png", confidence=0.9)))
    except:
            pass
    try:
        if locateOnScreen("static\\full.png", confidence=0.9):
            click(center(locateOnScreen("static\\full.png", confidence=0.9)))
    except:
            pass

    try:
        if locateOnScreen("static\\lpt.png", confidence=0.9):
            click(center(locateOnScreen("static\\lpt.png", confidence=0.9)))
    except:
            pass
    
    return ''