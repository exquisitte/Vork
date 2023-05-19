import jwt


class VerifyToken:
    def __init__(self, token):
        self.token = token

    def verify(self, secret_key, algorithm):
        try:
            decoded_token = jwt.decode(self.token, secret_key, algorithms=[algorithm])
            return decoded_token
        except jwt.exceptions.DecodeError:
            return {"status": False, "msg": "Invalid token"}
