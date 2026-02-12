from typing import Any, Dict, List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="IDS568 Module 3 - Milestone 2", version="1.0.0")


class PredictRequest(BaseModel):
    # Keep it generic: list of numeric features
    features: List[float] = Field(..., min_length=1)


class PredictResponse(BaseModel):
    prediction: float


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    """
    Minimal deterministic inference logic.
    For Milestone 2, the goal is containerization + CI/CD, not model accuracy.
    """
    # Simple "model": sum of inputs
    pred = float(sum(payload.features))
    return PredictResponse(prediction=pred)
