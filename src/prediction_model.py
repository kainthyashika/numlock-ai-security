import random

def predict_threat(phone):

    score = random.randint(0,100)

    if score < 40:
        risk = "LOW"

    elif score < 70:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    return score, risk
