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

@app.route("/prediction.html", endpoint='prediction')
def prediction():
    return render_template('/prediction.html')

@app.route("/no_pd.html", endpoint='no_pd')
def no_pd():
    return render_template('no_pd.html')

@app.route("/severity.html", endpoint='severity')
def no_pd():
    return render_template('severity.html')
    

@app.route('/prediction.html', methods=['GET','POST'])
def detection():
    g = request.form['gender']
    if g == 'female':
        gender = 1
    else:
        gender = 0
    a = request.form['age']
    if a == 'young':
        age = 0
    else: 
        if a == '41-50':
            age = 1
        if a == '51-60':
            age = 2
        if a == '61-70':
            age = 3
        if a == '71-80':
            age = 4
        if a =="80+":
            age = 5
    arr = np.array([[gender, age]])
    pred = model.predict(arr)
    print(pred)
    return render_template('prediction.html',data=pred)


if __name__ == "__main__":
    app.run(debug=True)


