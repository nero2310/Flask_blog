from flask import jsonify


class UserModel:
    def __init__(self, name="anonymus", email="anonymus", password="anonymus"):
        self.name = name.data
        self.email = email.data
        self.password = password.data

    def signup(self):
        user = {
            "_id": "",
            "name": self.name,
            "email": self.email,
            "password_hash": self.password  # toDo generate hash from password
        }
        print(user)
        return jsonify(user), 200

    # @property
    # def hash(self):
        # return
