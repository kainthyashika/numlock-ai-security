from risk_engine import calculate_risk
from fraud_engine import fraud_score
from honeypot_engine import honeypot_response
from privacy_guard import adaptive_disclosure
from notifier import send_alert

def monitor_system():

    risk_map = calculate_risk()

    for phone, risk in risk_map.items():

        fraud = fraud_score(phone)

        if fraud > 70:

            print("HONEYPOT TRIGGERED")

            response = honeypot_response()

            send_alert(
            f"⚠️ Cyber Threat Detected\nPhone: {phone}\nFraud Score: {fraud}"
            )

        else:

            data = "123456789012"

            response = adaptive_disclosure(data, risk)

        print("Phone:", phone)
        print("Risk:", risk)
        print("Fraud Score:", fraud)
        print("Response:", response)
        print("------")

if __name__ == "__main__":
    monitor_system()
