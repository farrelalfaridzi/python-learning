from core.character import Character

from core.item import Item

from core.weapon import Weapon

from core.player import Player

from core.monster import Monster

from core.inventory import Inventory

from core.potion import Potion

player = Player("Farrel", 100, 50, None)
wood = Weapon("Wood Sword",15,10)
small = Potion("small potion",10,10)
monster = Monster("Goblin",100,30,small)

player.buy(wood)
player.equip(wood)
player.attack(monster)
monster.attack(player)
player.buy(small)
player.drink(small)
player.status()
monster.status()