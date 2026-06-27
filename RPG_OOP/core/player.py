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
        monster.take_damage(self.weapon.damage)
        print(f"{self.nama} menyerang!")

    def equip(self, weapon_baru):
        if self.weapon != None:
            self.inventory.add_item(self.weapon)
        self.weapon = weapon_baru