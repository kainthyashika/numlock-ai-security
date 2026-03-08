import time

REQUEST_HISTORY = {}

def fraud_score(phone):

    now = time.time()

    history = REQUEST_HISTORY.get(phone, [])

    history = [t for t in history if now - t < 60]

    history.append(now)

    REQUEST_HISTORY[phone] = history

    score = min(len(history)*20, 100)

    return score
