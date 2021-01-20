class Character:
    def __init__(self, health=1, power=1):
        self.health = health
        self.power = power
    
    # def status(self):
            # if self.health > 0:
                # print(f"You have {self.health} health and {self.power} power.")
    
    def alive(self):
        while self.health > 0:
            return True

class Hero(Character):
    def __init__(self, health = 10, power = 5):
        super().__init__(10, 5)
        self.power = power
        self.health = health
    
    def attack(self, goblin):
        goblin.health -= self.power

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