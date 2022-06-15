import os

from project.config import BASEDIR, DevelopmentConfig, TestingConfig
from project.server import create_app


class TestConfig:
    def test_development(self):
        app_config = create_app(DevelopmentConfig).config
        assert app_config["TESTING"] is False
        assert app_config["DEBUG"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///" + os.path.join(
            os.path.dirname(BASEDIR), "project.db"
        )
        assert app_config["SQLALCHEMY_ECHO"] is True

    def test_testing(self):
        app_config = create_app(TestingConfig).config
        assert app_config["TESTING"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
