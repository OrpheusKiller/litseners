# from pyautogui import locateOnScreen, click, center
from flask import Flask, render_template
from webbrowser import open
from time import sleep

app = Flask(__name__)

@app.route("/")
def frontend():
    return render_template('index.html')
sleep(5)
@app.route("/litseners")

def litseners():
    open("https://www.youtube.com/watch?v=oWsnhdwJ_Vw")