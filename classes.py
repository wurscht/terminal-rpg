class Character():
    def __init__(self, hp, strength):
        self.hp = hp
        self.strength = strength

    def get_damage(self, enemy_strength):
        damage = int(enemy_strength * 1)
        self.hp = int(self.hp - damage)
        print("")
        print("\033[1;31;40mYou received {0} damage\033[0m".format(damage))
        print("\033[1;31;40mYour hp fell to {0}\033[0m".format(self.hp))


class Player(Character):
    def __init__(self, hp, strength, vitality, exp, lvl, inventory):
        self.hp = hp
        self.strength = strength
        self.vitality = vitality
        self.exp = exp
        self.lvl = lvl
        self.inventory = inventory


class Creature(Character):
    def get_damage(self, enemy_strength):
        damage = int(enemy_strength * 1)
        self.hp = int(self.hp - damage)
        print("")
        print(
            "\033[1;32;40mThe enemy received {0} damage\033[0m".format(damage)
        )
        print(
            "\033[1;32;40mThe enemy's hp fell to {0}\033[0m".format(self.hp)
        ) 


class Item():
    def __init__(self, name, stre, hp, cost):
        self.name = name
        self.str = stre
        self.hp = hp
        self.cost = cost
