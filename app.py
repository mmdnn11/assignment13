from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.joblib")

@app.post("/predict/")
def predict(features: dict):
    data = pd.DataFrame([features])
    prediction = model.predict(data)
    return {"prediction": prediction[0]}

