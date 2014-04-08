# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return "Hello %s!" % name

@app.route('/hola/<nombre>')
def hola(nombre):
    return u"¡Hola %s!" % nombre
