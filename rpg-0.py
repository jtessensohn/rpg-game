# from hero import Hero
# from goblin import Goblin
from character import Character, Hero, Goblin

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    goblin = Goblin()

    while goblin.alive() and my_hero.alive():
        my_hero.status()
        goblin.status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack(goblin)
            print("You do %d damage to the goblin." % my_hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(my_hero)
            print("The goblin does %d damage to you." % goblin.power)
            if my_hero.health <= 0:
                print("You are dead.")

main()
