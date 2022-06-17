import jwt
from flask import request
from flask_restx import abort
from flask import current_app


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer')[-1]
        try:
            jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['JWT_ALGO'])
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper
