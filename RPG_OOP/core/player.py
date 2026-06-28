from core.character import Character
from core.inventory import Inventory
class Player(Character):
    def __init__(self, nama, hp, gold, weapon, armor):
        super().__init__(nama, hp)
        self.gold = gold
        self.weapon = weapon
        self.armor = armor
        self.inventory = Inventory()

    def status(self):
        print("=== PLAYER ===")
        super().status()
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
        print(f"{self.nama} menyerang!")
        monster.take_damage(self.weapon.damage)

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