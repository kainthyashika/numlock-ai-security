import hashlib
import time

TOKENS = {}

def generate_token(phone, scope):

    base = f"{phone}-{scope}-{time.time()}"

    token = hashlib.sha256(base.encode()).hexdigest()[:16]

    TOKENS[token] = {
        "phone": phone,
        "scope": scope,
        "exp": time.time() + 300,
        "used": False
    }

    return token


def validate_token(token):

    info = TOKENS.get(token)

    if not info:
        return "INVALID"

    if info["used"]:
        return "USED"

    if time.time() > info["exp"]:
        return "EXPIRED"

    info["used"] = True

    return "VALID"
