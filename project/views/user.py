from flask_restx import abort, Namespace, Resource
from flask import request
from project.helper import auth_required
from project.services.user import UserService
from project.setup_db import db

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data_tokens = request.headers['Authorization']
        token = data_tokens.split('Bearer')[-1]
        user = UserService(db.session).get_user(token=token)
        return user, 200

    @auth_required
    def patch(self):
        data = request.json
        data_tokens = request.headers['Authorization']
        token = data_tokens.split('Bearer')[-1]
        if UserService(db.session).update_user(token=token, data=data):
            return '', 200
        else:
            abort(400)

    @auth_required
    def put(self):
        data = request.json
        data_tokens = request.headers['Authorization']
        token = data_tokens.split('Bearer')[-1]
        if ['password_1', 'password_2'] not in data.values():
            abort(400)
        password_1 = data['password_1']
        password_2 = data['password_2']
        if UserService(db.session).update_passwords(password_1, password_2, token):
            return '', 200
        else:
            abort(400)
