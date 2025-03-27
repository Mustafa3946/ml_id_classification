# Identity Document Classification

This project demonstrates how to build a simple machine learning model for classifying identity documents using SageMaker, TensorFlow, and Keras. The dataset consists of images representing various types of identity documents. This guide provides all the necessary steps to preprocess the dataset, train the model, evaluate its performance, and save the model.

## Project Structure
SageMaker-Id-Classification/ │ ├── images.zip # Dataset containing images of identity documents ├── tmp/ # Temporary folder for extracted images │ └── dataset/
│ └── images/ # Unzipped images dataset ├── model.py # Python script to build, train, and evaluate the model └── README.md


## Requirements

## Features
- Machine learning model for document classification
- I for image submission and prediction
- API for model inference
- Docker Compose setup for seamless deployment

he following libraries are required to run this project:

- `boto3`
- `sagemaker`
- `numpy`
- `tensorflow`
- `scikit-learn`
- `zipfile` (included in Python standard library)

```bash
pip install boto3 sagemaker tensorflow scikit-learn
```
## Dataset
The dataset (`images.zip`) contains images of identity documents, categorized into 10 classes:

- **alb_id** - ID Card of Albania
- **aze_passport** - Passport of Azerbaijan
- **esp_id** - ID Card of Spain
- **est_id** - ID Card of Estonia
- **fin_id** - ID Card of Finland
- **grc_passport** - Passport of Greece
- **lva_passport** - Passport of Latvia
- **rus_internalpassport** - Internal passport of Russia
- **srb_passport** - Passport of Serbia
- **svk_id** - ID Card of Slovakia
The dataset is provided as a ZIP file (images.zip) containing subfolders for each class, where each subfolder contains images representing the respective class.

## Steps
1. Data Preprocessing
Unzipping the dataset: The dataset (images.zip) is extracted to a temporary directory.

Image normalization: All image pixel values are normalized by dividing by 255.0 to scale the values between 0 and 1.

Data augmentation: We use ImageDataGenerator from Keras for real-time augmentation to improve the model's generalization ability.

2. Model Building
A Convolutional Neural Network (CNN) model is defined using Keras:

The model architecture consists of two convolutional layers, followed by max-pooling layers.

After flattening the output, a dense layer is used, and the final layer uses softmax activation to predict the class of each input image.

3. Model Training
The training dataset is divided into an 80% training set and a 20% validation set.

The model is trained for 10 epochs using the Adam optimizer and categorical crossentropy loss.

4. Model Evaluation
After training, the model is evaluated using the validation set. We calculate and display the classification report, which includes metrics such as precision, recall, F1-score, and accuracy.

5. Model Saving
Finally, the trained model is saved in Keras format (.keras), which can be loaded for future use or deployment.

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Docker
- Docker Compose
- Python 3.x (if running locally)
- Node.js & npm (if running frontend locally)

### Running with Docker Compose
To start all services:
```sh
docker-compose up --build
```

### Running Locally (Without Docker)
#### Backend Setup
```sh
cd backend
pip install -r requirements.txt
python app.py
```
#### Frontend Setup
```sh
cd frontend
npm install
npm start
```

## API Endpoints
- `POST /predict` - Accepts an image file and returns the predicted document class.

## Usage
1. Start the application.
2. Open the React UI in your browser.
3. Upload an image of an identity document.
4. View the predicted class returned by the model.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## Contact
For questions or support, open an issue in the repository.

