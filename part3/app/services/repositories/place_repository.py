from app.models.place import Place
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_places_by_owner(self, owner_id):
        return self.model.query.filter_by(owner_id=owner_id).all()

    def search_places_by_title(self, title):
        return self.model.query.filter(Place.title.ilike(f'%{title}%')).all()
