from project.config import DevelopmentConfig
from project.dao.models import Genre
from project.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }


if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)
