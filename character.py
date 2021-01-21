from random import randrange
class Character:
    def __init__(self, health=1, power=1):
        self.health = health
        self.power = power
    
    # def __str__(self):
    #     return 
    
    # def status(self):
    #         if self.health > 0:
    #             print(f"{self} {self.health} health and {self.power} power.")
    
    def alive(self):
        while self.health > 0:
            return True
    
    def attack(self, hero):
        hero.health -= self.power


class Hero(Character):
    def __init__(self, health = 10, power = 5):
        # super().__init__(10, 5)
        self.power = power
        self.health = health
    
    def attack(self, enemy):
        crit = randrange(5)
        if crit == 4:
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the goblin.")
        elif crit != 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")

    def status(self):
            if self.health > 0:
                print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        # super().__init__(6, 2)
        self.power = power
        self.health = health
    
    def __str__(self):
        return "Goblin"
    
    def status(self):
            if self.health > 0:
                print(f"The goblin has {self.health} health and {self.power} power.")

class Medic(Character):
    def __init__(self, health = 10, power = 2):
        self.health = health
        self.power = power
    
    def attack(self, hero):
        heal = randrange(5)
        if heal == 4:
            hero.health -= self.power
            self.health += 2
            print(f"{self} does {self.power} damage to you and healed for 2!")
        elif heal != 4:
            hero.health -= self.power
            print(f"{self} does {self.power} damage to the you.")

    def __str__(self):
            return "Medic"

    # def attack(self, hero):
    #     hero.health -= self.power
    #     self.health += 2

    def status(self):
        if self.health > 0:
            print(f"The medic has {self.health} health and {self.power} power.")

class Shadow(Character):
    def __init__(self, health = 1, power = 1):
        self.health = health
        self.power = power

    def __str__(self):
            return "Shadow"

    def status(self):
        if self.health > 0:
            print(f"The Shadow has {self.health} health and {self.power} power.")

class Zombie(Character):
    def __init__(self, health = 10, power = 1):
        self.health = health
        self.power = power

    def __str__(self):
            return "Zombie"

    def status(self):
        if self.health > 0:
            print(f"The Zombie has {self.health} health and {self.power} power.")