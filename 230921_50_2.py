# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:20:42 2023

@author: LGHERO
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hellow World!!"
    
    