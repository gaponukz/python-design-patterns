from __future__ import annotations
from dataclasses import dataclass
from factory import IStorage

@dataclass
class Entity:
    '''
    Add some `Entity` object for make example more real-life
    '''
    name: str

    def __eq__(self, other: Entity):
        return self.name == other.name

class ListClientsDB(IStorage[Entity]):
    def __init__(self):
        self.clients: list[Entity] = []

    def add(self, item: Entity):
        self.clients.append(item)
    
    def remove(self, item: Entity):
        self.clients.remove(item)

    def get_all(self) -> list[Entity]:
        return self.clients

class DictClientsDB(IStorage[Entity]):
    def __init__(self):
        self.clients: dict[str, Entity] = {}

    def add(self, item: Entity):
        self.clients[item.name] = item
    
    def remove(self, item: Entity):
        del self.clients[item.name]

    def get_all(self) -> list[Entity]:
        return list(self.clients.values())

def logic(db: IStorage[Entity]):
    entity = Entity("Anton")

    db.add(entity)
    assert len(db.get_all()) == 1
    db.remove(entity)
    assert len(db.get_all()) == 0

if __name__ == "__main__":
    '''
    We can use both databases!
    Dependency inversion principle implementation:
        High-level modules should depend on abstractions
        rather than concrete implementations.
    '''
    list_db = ListClientsDB()
    dict_db = DictClientsDB()

    logic(list_db)
    logic(dict_db)
