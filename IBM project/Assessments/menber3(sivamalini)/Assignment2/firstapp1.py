# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:48:21 2022

@author: Ashraf
"""

from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"
if __name__ =="__main__":
    app.run()