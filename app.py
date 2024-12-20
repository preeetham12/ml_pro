from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize the FastAPI app
app = FastAPI()

# Load the saved model
model = joblib.load("final_model.pkl")

# Define input data schema
class InputData(BaseModel):
    age: float
    menopause: str
    tumor_size: float
    node_caps: str
    breast: str
    breast_quad: str

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert input data into the required format
    input_features = np.array([[
        data.age,
        data.menopause,
        data.tumor_size,
        data.node_caps,
        data.breast,
        data.breast_quad,
    ]])

    # Perform prediction
    prediction = model.predict(input_features)
    probability = model.predict_proba(input_features).max()

    return {"result": int(prediction[0]), "probability": probability}
