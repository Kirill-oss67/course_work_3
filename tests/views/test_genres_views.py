import pytest

from project.dao.models import Genre


class TestGenresView:
    url = "/genres/"

    @pytest.fixture
    def genre(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genres(self, client, genre):
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json == [
            {"id": genre.id, "name": genre.name},
        ]


class TestGenreView:
    url = "/genres/{genre_id}"

    @pytest.fixture
    def genre(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genre(self, client, genre):
        response = client.get(self.url.format(genre_id=genre.id))
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name}

    def test_genre_not_found(self, client):
        response = client.get(self.url.format(genre_id=1))
        assert response.status_code == 404
