class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
    
    def eat_treat(self, treat):
        self.fullness += treat.yum
        self.happiness += treat.joy
    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()
    
    def get_toy(self, toy):
        self.toys.append(toy)

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()