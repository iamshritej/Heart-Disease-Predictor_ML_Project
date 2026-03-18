from fastapi import FastAPI
from Backend.predict import predict_output

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    return predict_output(data)