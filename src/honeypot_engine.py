import random

def honeypot_response():

    fake_data = [
        "XXXX-XXXX-1111",
        "XXXX-XXXX-2222",
        "XXXX-XXXX-3333"
    ]

    return random.choice(fake_data)
