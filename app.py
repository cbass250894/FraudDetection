from tkinter.font import names
import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST',"GET"])

def predict():
    '''
    For rendering results on HTML GUI
    '''
    def preds(amount, age,city,carmake,carmodel,
                gender,employmentstatus,collisionstate,collisiondamage):
        
        return predict
        
    Amount =request.form.get("Amount")
    Age =request.form.get("Age")
    City =request.form.get("City")
    Gender =request.form.get("Gender")
    employmentstatus = request.form.get("employmentstatus") 
    collisionstate = request.form.get("collisionstate") 
    collisiondamage = request.form.get("collisiondamage") 
       
    render_template('index.html',prediction = predict)
    prediction = 20
    output = request.form.to_dict()
    name = output["name"]
    return render_template("index.html",name = name)


if __name__ == "__main__":
    app.run(debug=True)
