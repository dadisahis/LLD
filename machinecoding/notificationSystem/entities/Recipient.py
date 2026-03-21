class Recipient:
    def __init__(self, user_id, email, token, phonenumber):
        self._user_id = user_id
        self._email = email
        self._token = token
        self._phone_number = phonenumber

    def get_user_id(self):
        return self._user_id
    def get_email(self):
        return self._email
    def get_token(self):
        return self._token
    def get_phone_no(self):
        return self._phone_number
        