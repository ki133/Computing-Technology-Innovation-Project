# delay_prediction.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

# Define base directory for consistent absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model and encoder paths
DELAY_MODEL_PATH = os.path.join(BASE_DIR, "Model/trained_models/flight_delay_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "Model/trained_models/encoder.pkl")

# Load model and encoder
try:
    delay_model = joblib.load(DELAY_MODEL_PATH)
    delay_encoder = joblib.load(ENCODER_PATH)
    print("Delay model and encoder loaded successfully.")
except Exception as e:
    print(f"Error loading model or encoder: {e}")

# Initialize FastAPI router
router = APIRouter()

# Define input data model
class DelayPredictionInput(BaseModel):
    airline: str
    departing_port: str
    arriving_port: str
    month: int
    year: int

# Define prediction endpoint
@router.post("/predict")
def predict_delay(input_data: DelayPredictionInput):
    try:
        # Prepare input data
        data = pd.DataFrame([input_data.dict()])
        data_encoded = pd.DataFrame(
            delay_encoder.transform(data[['airline', 'departing_port', 'arriving_port']]),
            columns=delay_encoder.get_feature_names_out(['airline', 'departing_port', 'arriving_port'])
        )
        input_features = pd.concat([data[['month', 'year']].reset_index(drop=True), data_encoded], axis=1)
        
        # Ensure columns match model input
        input_features = input_features.reindex(columns=delay_model.classes_, fill_value=0)
        
        # Predict delay
        prediction_probabilities = delay_model.predict_proba(input_features)
        is_delayed = prediction_probabilities[0][1] >= 0.5
        return {"is_delayed": bool(is_delayed), "probability_of_delay": prediction_probabilities[0][1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
