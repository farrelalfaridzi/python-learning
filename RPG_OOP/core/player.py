from core.character import Character
from core.inventory import Inventory
class Player(Character):
    def __init__(self, nama, hp, gold=0, weapon=None, armor=None):
        super().__init__(nama, hp)
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.inventory = Inventory()
        self.level = 1
        self.exp = 0
        self.bonus_damage = 0

    def status(self):
        print("=== PLAYER ===")
        super().status()
        print("Level :", self.level)
        print("EXP :", self.exp)
        print("Gold :", self.gold)
        if self.weapon != None:
            print("Weapon :", self.weapon.nama)
            print("Damage Weapon :", self.weapon.damage)
        else:
            print("Weapon :", None)
        if self.armor != None:
            print("Armor :", self.armor.nama)
            print("Armor Defense :", self.armor.defense)
        else:
            print("Armor :", None)

    def attack(self, monster):
        if self.weapon == None:
            print("Tidak ada weapon yang digunakan")
        else:
            print(f"{self.nama} menyerang!")
            damage_total = self.weapon.damage + self.bonus_damage
            monster.take_damage(damage_total)

    def equip_weapon(self, weapon_baru):
        if self.inventory.has_item(weapon_baru):
            if self.weapon != None:
                self.inventory.add_item(self.weapon)
            self.weapon = weapon_baru
            self.inventory.remove_item(weapon_baru)
            print(f"{weapon_baru.nama} berhasil di gunakan")
        else:
            print("weapon tidak ada di inventory")

    def equip_armor(self, armor_baru):
        if self.inventory.has_item(armor_baru):
            if self.armor != None:
                self.inventory.add_item(self.armor)
            self.armor = armor_baru
            self.inventory.remove_item(armor_baru)
            print(f"{armor_baru.nama} berhasil digunakan")
        else:
            print("armor tidak ada di inventory")

    def drink(self, potion):
        if self.inventory.has_item(potion):
            self.heal(potion.heal)
            self.inventory.remove_item(potion)
            print(f"{potion.nama} berhasil diminum")
        else:
            print("potion tidak ada di inventory")

    def buy(self, item):
        if self.gold < item.harga:
            print("gold tidak cukup")
        else:
            self.gold -= item.harga
            self.inventory.add_item(item)
            print(f"{item.nama} berhasil dibeli")

    def gain_exp(self, exp):
        self.exp += exp
        print(f"{self.nama} mendapatkan exp + {exp}")
        while self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        print("LEVEL UP!")
        self.exp -= 100
        print(f"Level sekarang : {self.level}")
        self.bonus_damage += 5
        print("bonus damage +5")