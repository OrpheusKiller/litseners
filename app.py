from pyautogui import locateOnScreen, click, center
from flask import Flask, render_template
from webbrowser import open

app = Flask(__name__)

@app.route("/")
def frontend():
    return render_template('index.html')

@app.route("/litseners")

def litseners():
    open("https://www.youtube.com/watch?v=oWsnhdwJ_Vw")