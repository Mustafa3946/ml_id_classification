# Identity Document Classification

This project demonstrates how to build a simple machine learning model for classifying identity documents using SageMaker, TensorFlow, and Keras. The dataset consists of images representing various types of identity documents. This guide provides all the necessary steps to preprocess the dataset, train the model, evaluate its performance, and save the model.

## Project Structure
The project is organized as follows:

- **SageMaker-Id-Classification/**
  - **images.zip**: Dataset containing images of identity documents.
  - **tmp/**: Temporary folder for extracted images.
    - **dataset/images/**: Unzipped images dataset.
  - **model.py**: Python script to build, train, and evaluate the model.
  - **README.md**: Project documentation.

## Requirements

## Features

The following libraries are required to run this project:

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
### Data Preprocessing

- **Unzipping the dataset**: The dataset (`images.zip`) is extracted to a temporary directory.
- **Image normalization**: All image pixel values are normalized by dividing by 255.0 to scale the values between 0 and 1.
- **Data augmentation**: I use `ImageDataGenerator` from Keras for real-time augmentation to improve the model's generalization ability.

### Model Building

A Convolutional Neural Network (CNN) model is defined using Keras:

- The model architecture consists of two convolutional layers, followed by max-pooling layers.
- After flattening the output, a dense layer is used, and the final layer uses softmax activation to predict the class of each input image.

### Model Training

- The training dataset is divided into an 80% training set and a 20% validation set.
- The model is trained for 10 epochs using the Adam optimizer and categorical crossentropy loss.

### Model Evaluation

After training, the model is evaluated using the validation set. I calculate and display the classification report, which includes metrics such as precision, recall, F1-score, and accuracy.

### Model Saving

The trained model is saved in Keras format (`.keras`), which can be loaded for future use or deployment.


# Getting Started

## Project Structure

The project consists of the following components:

- **Frontend**: A React application that allows users to upload images of documents.
- **Backend**: A Flask API that serves the machine learning model to classify the documents.
- **Machine Learning Model**: A TensorFlow model that classifies different types of ID documents.

The code for these components is located in the following directories:

- `frontend/`: The React frontend code.
- `flask_backend/`: The Flask backend code and model.
- `docker/`: Docker configuration files (including Dockerfiles and Docker Compose setup).

### Step 1: Clone the repository

```bash
git clone https://github.com/Mustafa3946/ml_id_classification.git
cd ml_id_classification
```

### Build the model using ml_id_classifier_tf.ipynb
This will generate the document_classifier.keras model file in the root of the project directory.

### Move the model to the backend folder
After building the model, move it to the flask_backend/ folder:
```bash
mv document_classifier.keras flask_backend/
```

### Step 2: Build and Run the Services
Build the Docker containers for both the frontend and backend services using Docker Compose:
```bash
docker-compose up --build
```
This command will:

Build the frontend React application Docker container.

Build the Flask backend Docker container.

Set up the required networking between both services.

The --build flag ensures that Docker rebuilds the containers if any changes were made to the Dockerfiles or the application code.

### Step 3: Access the Application
Once the services are running, open a web browser and navigate to the following URL:

    http://<public_ip>:3000/

This will display the ID Document Classifier web interface where you can upload images.

You should now be able to interact with the frontend, upload images of ID documents, and get predictions from the backend.

### Step 4: Stopping the Services
To stop the services, press CTRL + C in the terminal where you ran docker-compose up. Alternatively, you can run:
```bash
docker-compose down
```
This will stop and remove the running containers, networks, and volumes defined in the docker-compose.yml file.

You can find Dockerfile for Backend in backend/Dockerfile.
And, you can find Dockerfile for frontend Dockerfile for Frontend (frontend/Dockerfile)
