from core.character import Character

from core.item import Item

from core.weapon import Weapon

from core.player import Player

from core.monster import Monster

from core.inventory import Inventory

from core.potion import Potion

from core.armor import Armor

from game.battle import Battle

from game.shop import Shop

player = Player("Farrel", 100, 50, None, None)
wood = Weapon("Wood Sword",15,30)
small = Potion("small potion",10,10)
monster = Monster("Goblin",100,20,small,250)
leather = Armor("Leather armor",10,50)
battle = Battle(player, monster)
shop = Shop()
shop.add_item(wood)
shop.add_item(small)
shop.add_item(leather)

shop.open(player)
battle.start()