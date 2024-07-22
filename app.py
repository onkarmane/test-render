# app.py
from flask import Flask, request, jsonify
# import joblib

app = Flask(__name__)

# # Load a simple pre-trained model (for example purposes)
# model = joblib.load('model.pkl')

@app.route('/')
@app.route("/home/<'a'>")
def predict(a,b):
    return f"Welcome to my page {a} {b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
