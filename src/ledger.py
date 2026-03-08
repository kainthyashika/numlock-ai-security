import hashlib
import time

LEDGER = []

def record_consent(phone,purpose):

    data = f"{phone}-{purpose}-{time.time()}"

    hash_val = hashlib.sha256(data.encode()).hexdigest()

    block = {
        "phone":phone,
        "purpose":purpose,
        "hash":hash_val
    }

    LEDGER.append(block)

    return block
