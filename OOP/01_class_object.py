class Player:
    def __init__(self, nama, hp, gold, damage):
        self.nama = nama
        self.hp = hp
        self.gold = gold
        self.damage = damage

    def status(self):
        print("=== STATUS ===")
        print("Nama :", self.nama)
        print("HP :", self.hp)
        print("Gold :", self.gold)
        print("Damage :", self.damage)
        print("==============")

    def heal(self, heal_amount):
        self.hp += heal_amount

    def attack(self, monster):
        monster.hp -= self.damage

class Monster:
    def __init__(self, nama, hp, damage):
        self.nama = nama
        self.hp = hp
        self.damage = damage

    def status(self):
        print("=== MONSTER ===")
        print("Nama :", self.nama)
        print("HP :", self.hp)
        print("Damage :", self.damage)
        print("===============")

player = Player("Farrel", 100, 50, 20)
monster = Monster("Goblin", 100, 15)

player.attack(monster)
player.status()

monster.status()