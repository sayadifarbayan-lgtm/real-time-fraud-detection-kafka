import faust
import json
import pandas as pd
import joblib

# Load ML model
model = joblib.load("fraud_model.joblib")

# Create Faust app
app = faust.App(
    'fraud-detection-app',
    broker='kafka://localhost:9092',
    value_serializer='raw'
)

# Kafka topics
raw_topic = app.topic('raw-data')
predictions_topic = app.topic('predictions')

# Stream processing
@app.agent(raw_topic)
async def process(stream):

    async for event in stream:

        data = json.loads(event)

        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]

        result = {
            "prediction": int(prediction)
        }

        await predictions_topic.send(
            value=json.dumps(result).encode('utf-8')
        )

        print(f"Prediction sent: {result}")


if __name__ == '__main__':
    app.main()