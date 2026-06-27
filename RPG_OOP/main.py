class Character:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def status(self):
        print("Nama :", self.nama)
        print("HP :", self.hp)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"darah {self.nama} berkurang -{damage}")

class Item:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Weapon(Item):
    def __init__(self, nama,harga,damage):
        super().__init__(nama, harga)
        self.damage = damage

class Player(Character):
    def __init__(self, nama, hp, gold, weapon):
        super().__init__(nama, hp)
        self.gold = gold
        self.weapon = weapon
        self.inventory = Inventory()

    def status(self):
        print("=== PLAYER ===")
        super().status()
        print("Gold :", self.gold)
        print("Weapon :", self.weapon.nama)
        print("Damage Weapon :", self.weapon.damage)

    def attack(self, monster):
        monster.take_damage(self.weapon.damage)
        print(f"{self.nama} menyerang!")

    def equip(self, weapon_baru):
        if self.weapon != None:
            self.inventory.add_item(self.weapon)
        self.weapon = weapon_baru

class Monster(Character):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp)
        self.damage = damage

    def status(self):
        print("=== MONSTER ===")
        super().status()
        print("Damage :", self.damage)

    def attack(self, player):
        player.take_damage(self.damage)
        print(f"{self.nama} menyerang balik!")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        nomor = 0
        print("=== INVENTORY ===")
        for item in self.items:
            nomor += 1
            print(nomor, item.nama)
        print("=================")

player = Player("Farrel", 100, 50, None)
wood = Weapon("Wood Sword",15,10)
iron = Weapon("Iron Sword",20,15)
monster = Monster("Goblin",100,10)

player.equip(wood)
player.equip(iron)
player.attack(monster)
monster.attack(player)
player.status()
monster.status()
player.inventory.show_inventory()