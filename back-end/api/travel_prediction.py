# travel_prediction.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Define base directory for consistent absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
TRAVEL_MODEL_PATH = os.path.join(BASE_DIR, "Model/trained_models/travel_price_model.pkl")

# Load model
try:
    travel_model = joblib.load(TRAVEL_MODEL_PATH)
    print("Travel model loaded successfully.")
except Exception as e:
    print(f"Error loading travel model: {e}")

# Initialize FastAPI router
router = APIRouter()

# Define input data model
class TravelPredictionInput(BaseModel):
    year: int
    month: int
    hours_flown: float
    aircraft_km_flown: float
    aircraft_departures: float
    total_rev_pax_ud: float

# Define prediction endpoint
@router.post("/api/travel/predict")
def predict_travel(input_data: TravelPredictionInput):
    try:
        # Prepare input data
        data = pd.DataFrame([input_data.dict()])
        
        # Predict travel metric
        predicted_metric = travel_model.predict(data)
        return {"predicted_metric": predicted_metric[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
