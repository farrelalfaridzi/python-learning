from core.character import Character
from core.inventory import Inventory
class Player(Character):
    def __init__(self, nama, hp, gold=0, weapon=None, armor=None):
        super().__init__(nama, hp)
        self._gold = gold
        self._weapon = weapon
        self._armor = armor
        self.inventory = Inventory()
        self._level = 1
        self._exp = 0
        self._bonus_damage = 0
        self.is_defeated = False
        self.monster_defeated = 0
        self.battle_won = 0
        self.battle_lost = 0
        self.damage_dealt = 0
        self.damage_taken = 0
        self.potion_used = 0

    @property
    def gold(self):
        return self._gold
    @gold.setter
    def gold(self, value):
        self._gold = value
        if self._gold < 0:
            self._gold = 0

    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self, value):
        self._weapon = value

    @property
    def armor(self):
        return self._armor
    @armor.setter
    def armor(self, value):
        self._armor = value
        if self._armor.defense < 0:
            self._armor.defense = 0

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        self._level = value
        if self._level < 1:
            self._level = 1

    @property
    def exp(self):
        return self._exp
    @exp.setter
    def exp(self, value):
        self._exp = value

    @property
    def bonus_damage(self):
        return self._bonus_damage
    @bonus_damage.setter
    def bonus_damage(self, value):
        self._bonus_damage = value

    def status(self):
        print("=== PLAYER ===")
        super().status()
        print("Level :", self.level)
        print("EXP :", self.exp)
        print("Gold :", self.gold)
        print(f"Bonus damage : {self.bonus_damage}")
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
        print(f"Monster defeated : {self.monster_defeated}")
        print(f"Battle won : {self.battle_won}")
        print(f"Battle lost : {self.battle_lost}")
        print(f"Damage dealt : {self.damage_dealt}")
        print(f"Damage taken : {self.damage_taken}")
        print(f"Potion used : {self.potion_used}")

    def attack(self, monster):
        if self.weapon == None:
            print("Tidak ada weapon yang digunakan")
        else:
            print(f"{self.nama} menyerang!")
            damage_total = self.weapon.damage + self.bonus_damage
            monster.take_damage(damage_total)
            self.add_damage_dealt(damage_total)

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
            self.add_potion_used()
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

    def defeated(self):
        self.is_defeated = True

    def add_damage_taken(self, damage):
        self.damage_taken += damage

    def add_monster_defeated(self):
        self.monster_defeated += 1

    def add_battle_won(self):
        self.battle_won += 1

    def add_battle_lost(self):
        self.battle_lost += 1

    def add_damage_dealt(self, damage):
        self.damage_dealt += damage

    def add_potion_used(self):
        self.potion_used += 1