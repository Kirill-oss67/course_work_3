from project.dao.auth import AuthDao
import hashlib
import base64
from project.services.base import BaseService
from flask import current_app


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

    def register(self, email: str, password_hash: str):
        password_hash = self.__get_hash(password=password_hash)
        return AuthDao(self._db_session).create(email=email, password_hash=password_hash)
