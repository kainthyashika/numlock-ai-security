def mask_data(data):

    if len(data) > 4:
        return "X"*(len(data)-4) + data[-4:]

    return "****"


def adaptive_disclosure(data, risk):

    if risk == "LOW":
        return data

    if risk == "MEDIUM":
        return mask_data(data)

    if risk == "HIGH":
        return "ACCESS DENIED"
