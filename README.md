# Real-Time Credit Card Fraud Detection using Kafka & Faust

## Overview

This project builds a real-time streaming ML pipeline using:

- Apache Kafka
- Faust Streams API
- Python
- Random Forest Classifier

The application streams credit card transactions through Kafka and predicts whether each transaction is fraudulent in real time.

---

## Dataset

Credit Card Fraud Detection Dataset
Source:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## Machine Learning Model

Model:
RandomForestClassifier

Performance:

- Accuracy: 0.9995
- F1 Score: 0.8506

The model was trained offline and saved as:
fraud_model.joblib

---

## Project Components

### 1. Producer

Reads rows from the dataset and publishes them to the `raw-data` Kafka topic.

### 2. Streams Processor (Faust)

Consumes messages from `raw-data`,
runs the ML model,
and sends predictions to the `predictions` topic.

### 3. Consumer

Reads predictions from the `predictions` topic and prints them in real time.

---

## Technologies Used

- Python 3.10
- Apache Kafka
- Docker
- Faust
- scikit-learn
- pandas
- confluent-kafka

---

## Setup Instructions

### Install dependencies

```bash
pip install -r requirements.txt
```
