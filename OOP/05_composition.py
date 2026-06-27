class Weapon:
    def __init__(self, nama, damage):
        self.nama = nama
        self.damage = damage

class Player:
    def __init__(self, nama, hp, weapon):
        self.nama = nama
        self.hp = hp
        self.weapon = weapon

    def attack(self, monster):
        monster.hp -= self.weapon.damage
        if monster.hp < 0 :
            monster.hp = 0

    def equip(self, weapon_baru):
        self.weapon = weapon_baru

    def status(self):
        print("=== STATUS ===")
        print(self.nama)
        print("HP :", self.hp)
        print("Weapon :", self.weapon.nama)
        print("Damage weapon :", self.weapon.damage)
        print("==============")

class Monster:
    def __init__(self, nama, damage, hp):
        self.nama = nama
        self.damage = damage
        self.hp = hp

    def status(self):
        print("=== MONSTER ===")
        print(self.nama)
        print("Damage :", self.damage)
        print("HP :", self.hp)
        print("===============")

wood = Weapon("pedang kayu", 25)
iron = Weapon("iron sword",30)
player = Player("Farrel", 100, wood)
player.equip(iron)
monster = Monster("Goblin", 20, 100)

player.attack(monster)
player.status()
monster.status()