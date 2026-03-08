from sklearn.ensemble import IsolationForest
import joblib
from feature_engine import extract_features

MODEL_PATH = "../models/ai_detector.pkl"

def train_model():

    data = extract_features()

    model = IsolationForest(
        contamination=0.15,
        random_state=42
    )

    model.fit(data)

    joblib.dump(model, MODEL_PATH)

    print("AI model trained and saved")

if __name__ == "__main__":
    train_model()
