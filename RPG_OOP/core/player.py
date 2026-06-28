from core.character import Character
from core.inventory import Inventory
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
        print(f"{self.nama} menyerang!")
        monster.take_damage(self.weapon.damage)

    def equip(self, weapon_baru):
        if self.inventory.has_item(weapon_baru):
            if self.weapon != None:
                self.inventory.add_item(weapon_baru)
            self.weapon = weapon_baru
            print(f"{weapon_baru.nama} berhasil di gunakan")
        else:
            print("item tidak ada di inventory")

    def drink(self, potion):
        if self.inventory.has_item(potion):
            self.heal(potion.heal)
            self.inventory.remove_item(potion)
            print(f"{potion.nama} berhasil diminum")
        else:
            print("ption tidak ada di inventory")

    def buy(self, item):
        if self.gold < item.harga:
            print("gold tidak cukup")
        else:
            print(f"{item.nama} berhasil dibeli")
            self.gold -= item.harga
            self.inventory.add_item(item)