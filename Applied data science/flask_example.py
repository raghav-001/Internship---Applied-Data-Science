# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:48:48 2021

@author: Raghav
"""
from flask import Flask
app=Flask(__name__) # Flask object

# Functionalities to be written after object creation
@app.route('/') # / means home page
def hello():
    return ("Welcome")
@app.route('/data/') # Another path
def fun(): 
    print("New")
    return ("Debug call")

if __name__=='__main__':
    app.run(debug=True) # No need to restart server
# run it in anaconda prompt