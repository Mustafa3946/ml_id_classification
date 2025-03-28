# app.py
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

app = Flask(__name__)

# Load the pre-trained model
model_path = '/home/ec2-user/backend/document_classifier.h5'
model = load_model(model_path)

# Define the image size expected by the model
IMG_HEIGHT = 150
IMG_WIDTH = 150

@app.route('/predict', methods=['POST'])
def predict():

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

