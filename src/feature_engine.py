import pandas as pd

LOG_FILE = "../logs/activity.log"

def extract_features():

    df = pd.read_csv(
        LOG_FILE,
        names=["time","phone","action","status"]
    )

    grouped = df.groupby("phone")

    features = grouped.agg(
        request_count=("action","count"),
        failures=("status", lambda x: (x=="FAIL").sum())
    )

    return features
