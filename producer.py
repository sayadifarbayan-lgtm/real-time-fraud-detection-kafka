import pandas as pd
import json
import time
from confluent_kafka import Producer

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# Remove target column
features = df.drop("Class", axis=1)

print("Starting producer...\n")

# Send rows one by one
for index, row in features.iterrows():

    message = row.to_dict()

    producer.produce(
        'raw-data',
        value=json.dumps(message).encode('utf-8')
    )

    producer.flush()

    print(f"Sent record {index}")

    time.sleep(1)