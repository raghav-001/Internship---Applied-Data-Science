# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:58:51 2021

@author: Raghav
"""

from flask import Flask, request, render_template
from joblib import load

app=Flask(__name__)

column=load('onehot.save')
model=load('model.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST']) #url is directed to y_predict in index.html
def y_predict():
    x_test=[[x for x in request.form.values()]] # need to be stored in double array for transformation purpose
    print(x_test)
    x_test=column.transform(x_test) # apply transformation using the loaded transformer
    print(x_test)
    prediction=model.predict(x_test)
    print(prediction)
    output=prediction[0]
    print(output)
    return render_template('index.html',prediction_text='Profit {}'.format(output))
    

if __name__=='__main__':
    app.run(debug=True)
    