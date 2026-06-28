from core.character import Character

from core.item import Item

from core.weapon import Weapon

from core.player import Player

from core.monster import Monster

from core.inventory import Inventory

from core.potion import Potion

from core.armor import Armor

player = Player("Farrel", 100, 50, None, None)
wood = Weapon("Wood Sword",15,10)
small = Potion("small potion",10,10)
monster = Monster("Goblin",100,20,small)
leather = Armor("Leather armor",10,5)

player.buy(leather)
player.equip_armor(leather)
player.buy(wood)
player.equip_weapon(wood)
player.attack(monster)
monster.attack(player)
player.status()
monster.status()