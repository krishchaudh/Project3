# Project3
README: Hurricane Damage Classification Deployment

 Project Overview
This project uses a Convolutional Neural Network (LeNet-5) to classify post-hurricane satellite imagery into two categories: damage and no_damage. The model is deployed as a REST API using Flask, containerized with Docker, and served through docker-compose.

📁 Project Contents
Project3.ipynb: Complete Jupyter notebook with data preparation, training, and evaluation (Part 1 & 2).
Test.ipynb: Notebook for verifying and debugging inference manually.
lenet_best.keras: The trained model saved in Keras format.
server.py: Inference API code using Flask.
requirements.txt: Python libraries required for server.
Dockerfile: Docker image instructions.
docker-compose.yml: For building and running the Flask server.
Report.pdf: Written summary of work done (Part 4).

Running the Model via Docker
Step 1: Build and Run
docker-compose up --build
This builds the image and runs the Flask server on http://localhost:5000.
Step 2: Check Model Summary
curl http://127.0.0.1:5000/summary
Response:
{
  "model": "LeNet-5",
  "input_shape": [128, 128, 3],
  "output_shape": [1],
  "total_params": 1627961
}
Step 3: Inference
Send an image for classification:
curl -X POST http://127.0.0.1:5000/inference \
     -H "Content-Type: application/octet-stream" \
     --data-binary @sample.jpg
Expected Output:
{ "prediction": "damage" }

Docker Hub (If Using Remote Image)
If your model was pushed to Docker Hub:
docker pull krishchaudh/damage_classifier
docker run -p 5000:5000 krishchaudh/damage_classifier
Then test using the same /summary and /inference routes.

Model Info
Feature
Value
Model
LeNet-5
Input Shape
(128, 128, 3)
Output Classes
damage, no_damage
Best Accuracy
52%
F1-Score (damage)
0.39
Recall (damage)
0.45


Author
Krish Chaudhary
Electrical and Computer Engineering
The University of Texas at Austin
Spring 2025

