# -*- coding: utf-8 -*-

from flask import Flask
from crossdomain import crossdomain

app = Flask(__name__)

@app.route('/hello/<name>')
@crossdomain(origin='*')
def hello(name):
    return "Hello %s!" % name

@app.route('/hola/<nombre>')
@crossdomain(origin='*')
def hola(nombre):
    return u"¡Hola %s!" % nombre
