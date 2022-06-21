from sqlalchemy.orm.scoping import scoped_session
from project.dao.models.user import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def update_user(self, user, data):
        if 'name' in data:
            user['name'] = data.get('name')
        elif 'surname' in data:
            user['surname'] = data.get('surname')
        elif 'favorite_genre' in data:
            user['favorite_genre'] = data.get('favorite_genre')
        self._db_session.add(user)
        self._db_session.commit()


    def update_password(self,user, password_hash):
        user.password_hash = password_hash
        self._db_session.add(user)
        self._db_session.commit()