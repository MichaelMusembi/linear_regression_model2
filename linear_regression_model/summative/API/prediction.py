# prediction.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import os

# ==============================
# Load Best Model & Scaler
# ==============================

# Build absolute paths relative to this file
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "models", "scaler.pkl")

# Load model
model = joblib.load(MODEL_PATH)

# Load scaler only if file exists
scaler = joblib.load(SCALER_PATH) if os.path.exists(SCALER_PATH) else None

# ==============================
# FastAPI App
# ==============================
app = FastAPI(
    title="Glucose Level Prediction API",
    description="An API that predicts glucose levels using a trained ML model.",
    version="1.0"
)

# Allowed CORS (for Flutter App connection later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# Define Input Schema
# ==============================
class GlucoseInput(BaseModel):
    AGE: int = Field(..., ge=10, le=100, description="Age of the patient")
    GENDER: int = Field(..., ge=0, le=1, description="0 = Female, 1 = Male")
    WEIGHT: float = Field(..., ge=20, le=200, description="Weight in kg")
    SKIN_COLOR: int = Field(..., ge=1, le=3, description="Skin color code (1-3)")
    NIR_Reading: float = Field(..., ge=50, le=1000, description="Near Infrared Reading")
    HEARTRATE: float = Field(..., ge=20, le=200, description="Heart rate in bpm")
    HEIGHT: float = Field(..., ge=4.0, le=7.5, description="Height in feet")
    LAST_EATEN: float = Field(..., ge=0, le=24, description="Hours since last meal")
    DIABETIC: int = Field(..., ge=0, le=1, description="0 = Non-diabetic, 1 = Diabetic")
    HR_IR: float = Field(..., ge=10000, le=120000, description="HR Infrared Reading")

# ==============================
# Prediction Endpoint
# ==============================
@app.post("/predict")
def predict(input_data: GlucoseInput):
    # Convert input to numpy array
    features = np.array([[ 
        input_data.AGE,
        input_data.GENDER,
        input_data.WEIGHT,
        input_data.SKIN_COLOR,
        input_data.NIR_Reading,
        input_data.HEARTRATE,
        input_data.HEIGHT,
        input_data.LAST_EATEN,
        input_data.DIABETIC,
        input_data.HR_IR
    ]])

    # Apply standardization if scaler is available
    if scaler:
        features = scaler.transform(features)

    # Predict glucose level
    prediction = model.predict(features)[0]

    return {"predicted_glucose_level": round(float(prediction), 2)}
