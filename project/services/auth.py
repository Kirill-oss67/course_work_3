import jwt

from project.dao.auth import AuthDao
import hashlib
import base64
import hmac
from project.exceptions import UserNotFound, WrongPassword
from project.schemas.auth import UserCreatedSchema
from project.services.base import BaseService
from flask import current_app
from datetime import datetime, timedelta


class AuthService(BaseService):

    @staticmethod
    def __get_hash(password: str):
        hashed = hashlib.pbkdf2_hmac(
            hash_name=current_app.config["HASH_NAME"],
            salt=current_app.config['HASH_SALT'],
            iterations=current_app.config['HASH_ITERATIONS'],
            password=password.encode("utf-8")
        )
        return base64.b64encode(hashed).decode('utf-8')

    def register(self, email: str, password: str):
        password_hash = self.__get_hash(password=password)
        return AuthDao(self._db_session).create(email=email, password_hash=password_hash)

    @staticmethod
    def compare_passwords(password1, password2):
        return hmac.compare_digest(password1, password2)

    @staticmethod
    def generate_tokens(user):
        payload = {
            "email": user['email'],
            'id': user['id'],
            'exp': datetime.utcnow() + timedelta(minutes=current_app.config["TOKEN_EXPIRE_MINUTES"])
        }
        access_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGO'],
        )
        refresh_payload = {
            "email": user['email'],
            'id': user['id'],
            'exp': datetime.utcnow() + timedelta(days=current_app.config["TOKEN_EXPIRE_DAYS"])}
        refresh_token = jwt.encode(
            payload=refresh_payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGO'])

        return {
            'access_token': access_token,
            "refresh_token": refresh_token
        }

    def login(self, email: str, password: str):
        user = AuthDao.get_user_by_email(email=email,self=self)
        if user is None:
            raise UserNotFound

        password_hash = self.__get_hash(password=password)
        if not self.compare_passwords(user['password_hash'], password_hash):
            raise WrongPassword

        return self.generate_tokens(user)
