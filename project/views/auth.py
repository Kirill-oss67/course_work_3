from flask_restx import Namespace, Resource

from project.schemas.auth import AuthRegisterRequest
from project.setup_db import db
from project.services.auth import AuthService
from flask import request

auth_ns = Namespace('auth')


@auth_ns.route("/register/")
class RegisterView(Resource):
    def post(self):
        data = request.json
        new_data = AuthRegisterRequest().load(data)
        AuthService(db.session).register(
            email=new_data['email'],
            password=new_data['password'],
        )
        return "", 200


@auth_ns.route("/login/")
class LoginView(Resource):
    def post(self):
        data = request.json
        new_data = AuthRegisterRequest().load(data)
        tokens = AuthService(db.session).login(
            email=new_data['email'],
            password=new_data['password'],
        )
        return tokens, 200
