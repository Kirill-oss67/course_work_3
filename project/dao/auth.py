from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.user import User
from project.schemas.auth import UserCreatedSchema

class AuthDao():
    def __init__(self, session: scoped_session):
        self._db_session = session

    def create(self, email: str, password_hash: str):
        new_user = User(
            email=email,
            password_hash=password_hash,
        )
        self._db_session.add(new_user)
        self._db_session.commit()

        return UserCreatedSchema().dump(new_user)



