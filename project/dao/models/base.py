from project.setup_db import db


class BaseMixin(object):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
