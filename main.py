import os
import numpy as np
import xgboost as xgb
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google.cloud import storage

# ✅ Use direct path from mounted secret
SERVICE_ACCOUNT_PATH = "/gcp/gcp-key.json"
GCS_BUCKET_NAME = "penguin-models-2025"
GCS_BLOB_NAME = "model.json"

# Load the model from Google Cloud Storage
client = storage.Client()
bucket = client.get_bucket(GCS_BUCKET_NAME)
blob = bucket.blob(GCS_BLOB_NAME)

model_path = "/tmp/model.json"
blob.download_to_filename(model_path)

model = xgb.XGBClassifier()
model.load_model(model_path)

# Set up FastAPI
app = FastAPI(title="Penguin Species Predictor")

species_map = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}

class PenguinFeatures(BaseModel):
    bill_length_mm: float = Field(..., gt=0)
    bill_depth_mm: float = Field(..., gt=0)
    flipper_length_mm: float = Field(..., gt=0)
    body_mass_g: float = Field(..., gt=0)

@app.get("/")
def root():
    return {"message": "Welcome to the Penguin Predictor API!"}

@app.post("/predict")
def predict_species(features: PenguinFeatures):
    try:
        input_array = np.array([[
            features.bill_length_mm,
            features.bill_depth_mm,
            features.flipper_length_mm,
            features.body_mass_g
        ]])
        prediction = model.predict(input_array)[0]
        return {"prediction": species_map.get(int(prediction), "Unknown")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
