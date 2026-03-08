import os
from datetime import datetime

LOG_FILE = "../logs/activity.log"

def log_event(phone, action, status):
    os.makedirs("../logs", exist_ok=True)

    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    line = f"{ts},{phone},{action},{status}\n"

    with open(LOG_FILE, "a") as f:
        f.write(line)

    print("Logged:", line.strip())


if __name__ == "__main__":
    log_event("+919876543210","TOKEN_REQUEST","SUCCESS")
