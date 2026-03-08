USER_DB = {}

def register_user(phone, chat_id):

    USER_DB[phone] = chat_id

    return True


def get_chat_id(phone):

    return USER_DB.get(phone)
