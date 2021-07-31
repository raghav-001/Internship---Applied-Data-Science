# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:16:11 2021

@author: Raghav
"""

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def hello():
    return ("Hello")

@app.route('/admin')
def hello_admin():
    return ("Hello admin")

@app.route('/data/<id>') # Eg: type data/1234
def id_data(id):
    return ("Hello, your ID is %s" %id)

@app.route('/user/<name>')
def user_name(name):
    if name=="Raghav":
        return redirect(url_for('hello_admin')) # call route function
    else:
        return ("Your name is %s" %name)
    
if __name__=='__main__':
    app.run(debug=True)
