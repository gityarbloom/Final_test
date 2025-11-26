from random import randint

class Soldier:
    # id_choice = [randint(0, 9) for n in range(6)]

    def __init__(self, id, first_name:str, last_name: str, gender: str, state: str, distans: int, status: False):
        # self.id = "8"
        # self.id += "".join(self.id_choice)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.state = state
        self.distans = distans
        self.status = status

    def update_soldier_status(self, updated_status: bool):
        self.status = updated_status


class Room:
    def __init__(self):
        self.room = []

    def add_soldier(self, soldier: Soldier):
        self.room.append(soldier)
        soldier.update_soldier_status(True)


class Building:
    def __init__(self):
        self.building = [Room.room for room in range(10)]


class Base:
    def __init__(self):
        self.buildings = [Building.building for house in range(2)]