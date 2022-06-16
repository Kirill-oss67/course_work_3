from sqlalchemy import desc
from sqlalchemy.orm.scoping import scoped_session
from flask import current_app
from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Movie).filter(Movie.id == pk).one_or_none()

    def get_all(self, page=None, status=None):
        movies = self._db_session.query(Movie)
        if status == "new":
            movies = movies.order_by(desc(Movie.year))
        if page:
            page = int(page)
            movies = movies.limit(current_app.config['ITEMS_PER_PAGE']). \
                offset(page * current_app.config['ITEMS_PER_PAGE'] - current_app.config['ITEMS_PER_PAGE'])
        return movies.all()
