import json
from app.models.user import User
from app.models.amenity import Amenity
from app.models.city import City
from app.models.country import Country
from app.models.place import Place
from app.models.review import Review

class DataManager:
    def __init__(self, storage_file='storage.json'):
        self.storage_file = storage_file
        self.__data = {}
        self.reload()

    def reload(self):
        try:
            with open(self.storage_file, 'r') as f:
                self.__data = json.load(f)
        except FileNotFoundError:
            self.__data = {}

    def save_to_file(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.__data, f)

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.__data:
            self.__data[entity_type] = {}
        self.__data[entity_type][entity.id] = entity.to_dict()
        self.save_to_file()

    def get(self, entity_id, entity_type):
        if entity_type in self.__data and entity_id in self.__data[entity_type]:
            data = self.__data[entity_type][entity_id]
            if entity_type == 'User':
                return User(**data)
            elif entity_type == 'Amenity':
                return Amenity(**data)
            elif entity_type == 'City':
                return City(**data)
            elif entity_type == 'Country':
                return Country(**data)
            elif entity_type == 'Place':
                return Place(**data)
            elif entity_type == 'Review':
                return Review(**data)
        return None

    def get_all(self, entity_type):
        if entity_type in self.__data:
            return [self.get(k, entity_type) for k in self.__data[entity_type]]
        return []

    def delete(self, entity_id, entity_type):
        if entity_type in self.__data and entity_id in self.__data[entity_type]:
            del self.__data[entity_type][entity_id]
            self.save_to_file()
            return True
        return False
