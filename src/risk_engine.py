import joblib
from feature_engine import extract_features

MODEL_PATH = "../models/ai_detector.pkl"

def calculate_risk():

    model = joblib.load(MODEL_PATH)

    features = extract_features()

    predictions = model.predict(features)

    risk = {}

    for phone, pred in zip(features.index, predictions):

        if pred == -1:
            risk[phone] = "HIGH"
        else:
            risk[phone] = "LOW"

    return risk
