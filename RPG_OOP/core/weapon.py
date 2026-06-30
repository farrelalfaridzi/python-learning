from core.item import Item
class Weapon(Item):
    def __init__(self, nama,harga,damage):
        super().__init__(nama, harga)
        self.damage = damage

    def use(self, player):
        player.equip_weapon(self)