from fastapi import FastAPI
from pydantic import BaseModel
from Backend.predict import predict_output

app = FastAPI()

class InputData(BaseModel):
    data: list

@app.get("/")
def home():
    return {"message": "Machine Output Prediction API Running"}

@app.post("/predict")
def predict(input_data: InputData):
    result = predict_output(input_data.data)
    return {"Predicted Parts Per Hour": result}