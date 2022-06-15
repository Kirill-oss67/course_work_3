from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Director).filter(Director.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Director).all()
