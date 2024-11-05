# price_prediction.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Define base directory for consistent absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model and encoder paths
PRICE_MODEL_PATH = os.path.join(BASE_DIR, "Model/trained_models/price_model.pkl")
PRICE_ENCODER_PATH = os.path.join(BASE_DIR, "Model/trained_models/price_encoder.pkl")

# Load model and encoder
try:
    price_model = joblib.load(PRICE_MODEL_PATH)
    price_encoder = joblib.load(PRICE_ENCODER_PATH)
    print("Price model and encoder loaded successfully.")
except Exception as e:
    print(f"Error loading price model or encoder: {e}")

# Initialize FastAPI router
router = APIRouter()

# Define input data model
class PricePredictionInput(BaseModel):
    year: int
    month: int
    port1: str
    port2: str
    route: str

# Define prediction endpoint
@router.post("/api/price/predict")
def predict_price(input_data: PricePredictionInput):
    try:
        # Prepare input data
        data = pd.DataFrame([input_data.dict()])
        data_encoded = pd.DataFrame(
            price_encoder.transform(data[['port1', 'port2', 'route']]),
            columns=price_encoder.get_feature_names_out(['port1', 'port2', 'route'])
        )
        input_features = pd.concat([data[['year', 'month']].reset_index(drop=True), data_encoded], axis=1)
        
        # Predict price
        predicted_price = price_model.predict(input_features)
        return {"predicted_price": predicted_price[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
