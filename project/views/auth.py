from flask_restx import Namespace, Resource, abort

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

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')
        if refresh_token is None:
            abort(400)
        tokens = AuthService(db.session).refresh_token(refresh_token)
        return tokens, 200
