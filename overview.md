### Overview
This script builds a simple image classification model to recognize different types of identity documents. It uses TensorFlow (Keras) for training a Convolutional Neural Network (CNN) and SageMaker for deployment. The model is trained on a dataset of identity document images stored in a ZIP file.

### Step-by-Step Breakdown
- Set Up SageMaker
The script initializes a SageMaker session and retrieves the execution role.

SageMaker is Amazon’s machine learning service, which allows us to train and deploy models in the cloud.

- Extract the Dataset
The dataset is provided as a ZIP file (images.zip).

If it's not already extracted, the script unzips it into the tmp/dataset/images folder.

- Define Image Parameters
Image Size: The input images are resized to 150x150 pixels.

Batch Size: The model processes 32 images per batch during training.

- Load and Preprocess Data
We use ImageDataGenerator to:

Rescale pixel values (normalize them between 0 and 1).

Split the dataset (80% for training, 20% for validation).

The dataset is then loaded using flow_from_directory(), which automatically assigns labels based on folder names.

- Build the CNN Model
The model consists of:

Two convolutional layers (Conv2D with ReLU activation) to detect image features.

MaxPooling layers to reduce spatial dimensions.

A Flatten layer to convert the feature maps into a 1D vector.

Two dense (fully connected) layers:

One hidden layer with 128 neurons and ReLU activation.

One output layer with softmax activation (for multi-class classification).

- Train the Model
The model is compiled using:

Adam optimizer (efficient for deep learning).

Categorical Crossentropy loss (since it’s a multi-class classification problem).

The model trains for 10 epochs with both training and validation data.

- Evaluate the Model
A batch of validation images is taken for evaluation.

The model predicts their class labels.

The true labels are extracted, and we calculate:

Classification report (precision, recall, and F1-score).

Overall accuracy.

- Save the Model
The trained model is saved in the recommended Keras format (.keras) instead of the legacy HDF5 format.