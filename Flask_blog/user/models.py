from flask import Flask, jsonify


class UserModel:

    def signup(self,name,email,password):
        user = {
            "_id": "",
            "name": name,
            "email": email,
            "password_hash":password # toDo generate hash from password
        }
        return jsonify(user), 200
