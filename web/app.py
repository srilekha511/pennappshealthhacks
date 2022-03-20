from flask import Flask, render_template, request
import numpy as np 
import pickle

import pandas as pd 
import numpy as np 

df = pd.read_csv('data.csv')

X = np.array(df[['age_group','sex']])
y = np.ravel(np.array(df[['diagnosis']]))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train, y_train)

import pickle
pickle.dump(sv, open('model.pkl','wb'))

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route("/index.html", endpoint='home')
def home():
    return render_template('index.html')

@app.route("/detection.html", endpoint='detect')
def detect():
    return render_template('detection.html')

@app.route("/", endpoint='index')
def index():
    return render_template('index.html')

@app.route("/learn.html", endpoint='learn')
def learn():
    return render_template('learn.html')






@app.route('/predict', methods=['POST'])
def detection():
    selectElement = document.querySelector('#gender')
    output = selectElement.value
    gender = document.querySelector('.output').textContent = output

    selectElement1 = document.querySelector('#age')
    output1 = selectElement.value
    age = document.querySelector('.output').textContent = output
   # age = request.form['age']
    arr = np.array([[gender, age]])
    pred = model.predict(arr)
    # send data to prediction.html file
    return render_template('prediction.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)


