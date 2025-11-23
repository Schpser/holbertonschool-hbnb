from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_user(self, user_id):
        return self.model.query.filter_by(user_id=user_id).all()

    def get_reviews_by_place(self, place_id):
        return self.model.query.filter_by(place_id=place_id).all()

    def get_average_rating(self, place_id):
        from sqlalchemy import func
        result = self.model.query.with_entities(
            func.avg(Review.rating)
        ).filter_by(place_id=place_id).scalar()
        return float(result) if result else 0.0
