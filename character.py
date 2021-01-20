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

class Hero(Character):
    def __init__(self, health = 10, power = 5):
        super().__init__(10, 5)
        self.power = power
        self.health = health
    
    def attack(self, goblin):
        crit = randrange(5)
        if crit == 4:
            goblin.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the goblin.")
        elif crit != 4:
            goblin.health -= self.power
            print("You do %d damage to the goblin." % self.power)

    def status(self):
            if self.health > 0:
                print(f"You have {self.health} health and {self.power} power.")

class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        super().__init__(6, 2)
        self.power = power
        self.health = health
    
    def attack(self, hero):
        hero.health -= self.power
    
    def status(self):
            if self.health > 0:
                print(f"The goblin has {self.health} health and {self.power} power.")

class Zombie(Character):
    def __init__(self, health = 10, power = 1):
        self.health = health
        self.power = power