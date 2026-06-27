from flask import Flask,request,render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
#load the model
model=pickle.load(open('spammailmodel.sav','rb'))

feature_extraction = pickle.load(open('spammailfeatureextractor.sav','rb')) 


@app.route('/')
def home():
    result = None
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST'])
def predict():
    
    Mail_Content=feature_extraction.transform([request.form['Mail_Content']])
    result=model.predict(Mail_Content)[0]
    prediction=None
    if result==0:
        prediction='Spam'
    else:
        prediction='Not Spam'
    return render_template('index.html',**locals()) 


if __name__ == '__main__':
   app.run(debug=True)