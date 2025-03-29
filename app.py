# app.py
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model, save_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image
import json

app = Flask(__name__)

# Load the pre-trained model
model_path = '/home/ec2-user/backend/document_classifier.keras'
if os.path.exists(model_path):
    print("Model file exists. Proceeding to load...")
    model = load_model(model_path, compile=False)
    print(model.summary())
else:
    print("Error: Model file does not exist at the specified path.")

    
# Define the image size expected by the model
IMG_HEIGHT = 150
IMG_WIDTH = 150

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Process the uploaded image
    img = Image.open(file.stream)
    img = img.resize((IMG_HEIGHT, IMG_WIDTH))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Get the class names
    class_names = list(model.class_names)

    return jsonify({
        'predicted_class': class_names[predicted_class],
        'confidence': predictions[0][predicted_class]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
