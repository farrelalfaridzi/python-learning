from core.character import Character

from core.item import Item

from core.weapon import Weapon

from core.player import Player

from core.monster import Monster

from core.inventory import Inventory

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