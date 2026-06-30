from core.item import Item

class Armor(Item):
    def __init__(self, nama, harga, defense):
        super().__init__(nama, harga)
        self.defense = defense

    def use(self, player):
        player.equip_armor(self)