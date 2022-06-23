from sqlalchemy.orm.scoping import scoped_session


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def update_user(self, user, data):
        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favourite_genre' in data:
            user.favorite_genre = data.get('favourite_genre')
        self._db_session.add(user)
        self._db_session.commit()

    def update_password(self, user, password_hash):
        user.password_hash = password_hash
        self._db_session.add(user)
        self._db_session.commit()
