import pickle
import numpy as np
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

# NEW (optional but recommended)
@app.route('/')
def home():
    return "Heart Disease API is running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    prediction = model.predict([data])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)