from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


#Route for a homepage
@app.route('/')
def index():
    return render_template('index.html')

#Route for a prediction page
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        pass