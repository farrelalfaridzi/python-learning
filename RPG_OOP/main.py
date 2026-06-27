class Weapon:
    def __init__(self, nama, damage, harga):
        self.nama = nama
        self.damage = damage
        self.harga = harga

class Player:
    def __init__(self, nama, hp, gold, weapon):
        self.nama = nama
        self.hp = hp
        self.gold = gold
        self.weapon = weapon

    def status(self):
        print("=== PLAYER ===")
        print("Nama :", self.nama)
        print("HP :", self.hp)
        print("Gold :", self.gold)
        print("Weapon :", self.weapon.nama)
        print("Damage Weapon :", self.weapon.damage)

    def attack(self, monster):
        monster.hp -= self.weapon.damage

    def equip(self, weapon_baru):
        self.weapon = weapon_baru

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

    def attack(self, player):
        player.hp -= self.damage

player = Player("Farrel", 100, 50, None)
wood = Weapon("Wood Sword",15,10)
monster = Monster("Goblin",100,10)

player.equip(wood)
player.attack(monster)
print("player menyerang!")
print("hp monster berkurang -",player.weapon.damage)
monster.attack(player)
print("monster menyerang balik!")
print("darah player berkurang -", monster.damage)
player.status()
monster.status()