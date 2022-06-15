from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def get_item_by_id(self, pk):
        director = DirectorDAO(self._db_session).get_by_id(pk)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)
