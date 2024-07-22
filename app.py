# app.py
from flask import Flask, request, jsonify
# import joblib

app = Flask(__name__)

# # Load a simple pre-trained model (for example purposes)
# model = joblib.load('model.pkl')

@app.route('/')
def predict():
    
    return "Welcome to my page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
