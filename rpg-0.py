# from hero import Hero
# from goblin import Goblin
from character import Character, Hero, Goblin, Medic, Shadow, Zombie
from random import randrange

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    enemy = randrange(4)
    if enemy == 0:
        enemy = Goblin()
    elif enemy == 1:
        enemy = Medic()
    elif enemy == 2:
        enemy = Shadow()
    elif enemy == 3:
        enemy = Zombie
    while enemy.alive() and my_hero.alive():
        my_hero.status()
        enemy.status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy}")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack(enemy)
            if enemy.health <= 0:
                print(f"The {enemy} is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.health > 0:
            # Goblin attacks hero
            enemy.attack(my_hero)
            print(f"The {enemy} does {enemy.power} damage to you.")
            if my_hero.health <= 0:
                print("You are dead.")

main()
