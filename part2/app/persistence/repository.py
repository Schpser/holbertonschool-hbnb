from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository:
    def __init__(self):
        self._storage = {}
    
    def add(self, entity):
        self._storage[entity.id] = entity
    
    def get(self, entity_id):
        return self._storage.get(entity_id)
    
    def get_all(self):
        """Get all entities"""
        return list(self._storage.values())
    
    def get_by_attribute(self, attr_name, attr_value):
        for entity in self._storage.values():
            if hasattr(entity, attr_name) and getattr(entity, attr_name) == attr_value:
                return entity
        return None
    
    def update(self, entity_id, updated_entity):
        if entity_id in self._storage:
            self._storage[entity_id] = updated_entity
            return True
        return False
    
    def delete(self, entity_id):
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False
    