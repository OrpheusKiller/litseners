from flask import Flask, render_template
from webbrowser import open

app = Flask(__name__)

@app.route("/")
def frontend():
    return render_template('index.html')

@app.route("/litseners")
def litseners():
    return '<script>window.location.href = "https://www.youtube.com/";</script>'
@app.route("/litsenrs")

def index():
    return '<script>window.location.href = "https://www.hello.com";</script>'