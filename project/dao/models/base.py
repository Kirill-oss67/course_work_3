from project.setup_db import db


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
