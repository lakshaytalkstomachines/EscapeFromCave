


class Enemy:
    def __init__(self):
        raise NotImplementedError("DO not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = " Giant Spider"
        self.hp = 10
        self.damage = 2
        self.agresive_level = 3 #from 1 - 3

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10


class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4
        self.agresive_level = 2 #from 1 - 3


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15
        self.agresive_level = 3 #from 1 - 3
        
class sheep(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 10
        self.damage = 0
        self.agresive_level = 1 #from 1 - 3
class cow(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 15
        self.damage = 0
        self.agresive_level = 1 #from 1 - 3
class electicity_dragon(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 300
        self.damage = 50
        self.agresive_level = 3 #from 1 - 3
