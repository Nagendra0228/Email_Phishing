from flask import Flask, render_template, request
import joblib

# Load the model and vectorizer
model = joblib.load('phishing_email_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)
    result = 'Phishing Email' if prediction[0] == 1 else 'Safe Email'
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
