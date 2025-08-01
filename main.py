import os
import numpy as np
import xgboost as xgb
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Load variables from .env file
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
GCS_BLOB_NAME = os.getenv("GCS_BLOB_NAME")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Set up Google Cloud Storage client using service account
client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
bucket = client.get_bucket(GCS_BUCKET_NAME)
blob = bucket.blob(GCS_BLOB_NAME)

# Download the model to a temp location and load it
model_path = "/tmp/model.json"
blob.download_to_filename(model_path)

model = xgb.XGBClassifier()
model.load_model(model_path)

# Create FastAPI app
app = FastAPI(title="Penguin Species Predictor")

# Label map
species_map = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}

# Input data structure using Pydantic
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
        species = species_map.get(int(prediction), "Unknown")
        return {"prediction": species}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
