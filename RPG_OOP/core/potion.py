from core.item import Item
class Potion(Item):
    def __init__(self, nama, harga, heal):
        super().__init__(nama, harga)
        self.heal = heal

    def use(self, player):
        player.drink(self)