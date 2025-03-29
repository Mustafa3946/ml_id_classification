import json
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import io

# Load model
model = tf.keras.models.load_model('document_classifier.keras')

# Load class names from the JSON file
with open('class_names.json', 'r') as f:
    class_names = json.load(f)

# Flask setup
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    file = request.files['file']
    
    # Preprocess the image
    # img = image.load_img(file, target_size=(150, 150))
    img = image.load_img(io.BytesIO(file.read()), target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    
    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]
    
    # Return the predicted class as JSON
    return jsonify({'predicted_class': predicted_class_name})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
