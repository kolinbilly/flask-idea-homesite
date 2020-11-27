"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from __init__ import app
from models import java_ap, java_hello, java_mvc, python_ap, python_flask, python_hello

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/java')
def java():
    return render_template("java.html")

@app.route('/java/hello')
def javahello():
    return render_template("project.html", data=java_hello())

@app.route('/java/mvc')
def javamvc():
    return render_template("project.html", data=java_mvc())

@app.route('/java/ap')
def javaap():
    return render_template("project.html", data=java_ap())

@app.route('/python')
def python():
    return render_template("python.html")

@app.route('/python/hello')
def pythonhello():
    return render_template("project.html", data=python_hello())

@app.route('/python/flask')
def pythonflask():
    return render_template("project.html", data=python_flask())

@app.route('/python/ap')
def pythonap():
    return render_template("project.html", data=python_ap())

@app.route('/about')
def about():
    return render_template("about.html")