import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict(request):
    request_json = request.get_json(silent=True)

    if not request_json or "features" not in request_json:
        return {"error": "Missing features"}, 400

    features = np.array(request_json["features"]).reshape(1, -1)
    prediction = int(model.predict(features)[0])

    return {"prediction": prediction}