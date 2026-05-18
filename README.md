# Real-Time Credit Card Fraud Detection using Kafka & Faust

## Overview

This project builds a real-time machine learning streaming pipeline using:

- Apache Kafka
- Faust Streams API
- Python
- Random Forest Classifier

The application streams credit card transaction data through Kafka and predicts whether each transaction is fraudulent in real time.

---

## Dataset

### Credit Card Fraud Detection Dataset

Source:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The dataset contains anonymized credit card transactions labeled as fraudulent or legitimate.

---

## Machine Learning Model

### Model Used

`RandomForestClassifier`

### Model Performance

- Accuracy: `0.9995`
- F1 Score: `0.8506`

The model was trained offline using scikit-learn and saved as:

```text
fraud_model.joblib
```

---

## Project Architecture

The system consists of three main components:

### 1. Producer

- Reads rows from the dataset
- Publishes transaction records to the Kafka topic:

```text
raw-data
```

### 2. Stream Processor (Faust)

- Consumes messages from the `raw-data` topic
- Loads the trained machine learning model
- Predicts fraud in real time
- Sends prediction results to the Kafka topic:

```text
predictions
```

### 3. Consumer

- Consumes prediction messages from the `predictions` topic
- Prints fraud prediction results in real time

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

## Project Files

```text
app.py                -> Faust stream processing application
producer.py           -> Kafka producer
consumer.py           -> Kafka consumer
train_model.py        -> ML model training script
fraud_model.joblib    -> Saved trained ML model
docker-compose.yml    -> Kafka & Zookeeper setup
requirements.txt      -> Python dependencies
README.md             -> Project documentation
```

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Start Kafka & Zookeeper

```bash
docker-compose up -d
```

---

### 3. Train the Machine Learning Model

```bash
python train_model.py
```

---

### 4. Start Faust Worker

```bash
py -3.10 -m faust -A app worker -l info
```

---

### 5. Run Producer

```bash
python producer.py
```

---

### 6. Run Consumer

```bash
python consumer.py
```

---

## Example Output

```text
Waiting for predictions...

Received Prediction: {'prediction': 0}
Received Prediction: {'prediction': 1}
```

Where:

- `0` = Normal transaction
- `1` = Fraudulent transaction

---

## Video Demo

Google Drive Demo Video:  
https://drive.google.com/file/d/17x2LrGSiBr0XxCJFZm64SOVHpaoHGrDa/view?usp=sharing

---

## GitHub Repository

Repository Link:  
https://github.com/sayadifarbayan-lgtm/real-time-fraud-detection-kafka
