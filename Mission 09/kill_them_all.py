class Character:

    def __init__(self, life=10, attack_point=10):
        self.life = life
        self.attack_point = attack_point

    def attack(self, target):
        target.get_hit(self.attack_point)

    def get_hit(self, damage):
        self.life -= damage


class Cratos(Character):

    def __init__(self):
        super().__init__(100, 10)
        self.experience = 0

    def gain_XP(self, amount):
        self.experience += amount
        self.attack_point += self.experience // 10
        self.experience %= 10


class Drauf(Character):

    def __init__(self, life, damage):
        super().__init__(life, damage)
