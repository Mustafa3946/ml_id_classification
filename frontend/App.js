import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://13.211.17.108:5000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setPrediction(response.data.predicted_class);
    } catch (error) {
      console.error("Error uploading file:", error);
      setPrediction("Error occurred while processing.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>ID Document Classifier</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: "10px" }}>Upload</button>
      <h3>Prediction: {prediction}</h3>
    </div>
  );
}

export default App;
