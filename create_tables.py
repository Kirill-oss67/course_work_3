from project.config import DevelopmentConfig
from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.dao.models.user import User
from project.server import create_app
from project.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
