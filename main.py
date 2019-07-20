import random
from classes import Player, Creature, Item


def main():
    player = choose_class()
    while player.hp > 0:
        enemy = spawn_enemy()
        if decide_what_to_do(player, enemy):
            fight(player, enemy)
        level_up(player)


def choose_class():
    char_class = input(
        """Choose a class for your character. (Warrior, Rogue or Wizard)\n""") # noqa
    if char_class == "Warrior":
        warrior = Player(100, 15, 13, 0, 1, [])
        print("You are a warrior (Hp: 100, Strength: 15, Vitality: 13)\n")
        return warrior
    elif char_class == "Rogue":
        rogue = Player(120, 10, 15, 0, 1, [])
        print("You are a rogue (Hp: 120, Strength: 10, Vitality: 15)\n")
        return rogue
    elif char_class == "Wizard":
        wizard = Player(100, 8, 10, 0, 1, [])
        print("You are a wizard (Hp: 100, Strength: 8, Vitality: 10)\n")
        return wizard
    else:
        print("That's not an available class. Try again.")


def spawn_enemy():
    enemy = Creature(random.randint(1, 10), random.randint(1, 10))
    print("An enemy appears\n")
    return enemy


def decide_what_to_do(player, enemy):
    answer = input("What do you want to do? (Run, Fight or Check inventory): ")
    if answer == "Run":
        result = random.randint(0, 10)
        if result > 5:
            print("\nYou were lucky and got away\n")
            return False
        else:
            print("\nThe enemy stands in your way\n")
            fight(player, enemy)
    if answer == "Fight":
        fight(player, enemy)
    if answer == "Check Inventory" or answer == "Check inventory" or answer == "Inventory": # noqa
        print("Your Inentory contains: {0}\n".format("".join(player.inventory))) # noqa


def fight(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        player.get_damage(enemy.strength)
        if player.hp <= 0:
            print("You died")
            break
        enemy.get_damage(player.strength)
        if enemy.hp <= 0:
            player.exp = player.exp + 10
            print("")
            print("\033[1;32;40mYou have defeated the enemy and gained 10 exp\033[0m")
            print("")
            loot(player)


def level_up(player):
    if player.exp >= 100 * player.lvl:
        player.lvl = player.lvl + 1
        player.strength = player.strength + player.lvl
        player.hp = player.hp + 20 + player.lvl
        print("-->Congratulation you have reached level {0}<--".format(player.lvl))


def loot(player):
    loot = create_items()
    if bool(random.getrandbits(1)):
        item = loot[random.randrange(len(loot))]
        print("You found a {0}".format(item.name))
        player.inventory.append(item)


def create_items():
    return [
        Item("Sword", 5, 0, 10),
        Item("Shield", 0, 5, 10),
        Item("Bow", 4, 2, 10),
        Item("Helmet", 0, 6, 10),
        Item("Dagger", 3, 3, 10)
    ]


main()
