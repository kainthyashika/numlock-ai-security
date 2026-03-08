import time

CONSENTS = {}

def request_consent(phone, purpose):

    consent_id = f"C{int(time.time()*1000)}"

    CONSENTS[consent_id] = {
        "phone": phone,
        "purpose": purpose,
        "approved": True,
        "timestamp": time.time()
    }

    return consent_id


def verify_consent(phone):

    for c in CONSENTS.values():
        if c["phone"] == phone and c["approved"]:
            return True

    return False
