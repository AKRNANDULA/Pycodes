from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello World!"

@app.route("/aditya")

def aditya():
    return "Hello Aditya!"

@app.route("/<string:name>")

def adi(name):
    name = name.capitalize()
    return f"<h1>Hello {name}}!</h1>"
