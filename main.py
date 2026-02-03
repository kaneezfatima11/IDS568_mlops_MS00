from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI(title="IDS568 Milestone 1 API")

# Load model once at startup
MODEL_PATH = Path(__file__).parent / "model.pkl"
model = joblib.load(MODEL_PATH)

class PredictRequest(BaseModel):
    features: list[float]  # expecting 4 numbers for iris

class PredictResponse(BaseModel):
    prediction: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    pred = model.predict([req.features])[0]
    return PredictResponse(prediction=int(pred))
