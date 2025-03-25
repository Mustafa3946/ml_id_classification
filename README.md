# Identity Document Classification

## Overview
This project builds a simple machine learning model for classifying identity documents based on images. The model is trained on a dataset containing 10 different classes of identity documents from various countries. A React-based user interface allows users to upload images and receive predictions. All components are wrapped in a Docker Compose configuration for easy deployment.

## Features
- Machine learning model for document classification
- I for image submission and prediction
- API for model inference
- Docker Compose setup for seamless deployment

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

## Project Structure
```
identity_doc_classification/
│── backend/                 # Machine learning model and API
│   ├── model.py             # Model training and inference
│   ├── app.py               # Flask/FastAPI application
│   ├── requirements.txt     # Backend dependencies
│── frontend/                # React-based user interface
│   ├── src/
│   ├── package.json         # Frontend dependencies
│── docker-compose.yml       # Docker Compose setup
│── Dockerfile.backend       # Backend Dockerfile
│── Dockerfile.frontend      # Frontend Dockerfile
│── README.md                # Project documentation
```

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

