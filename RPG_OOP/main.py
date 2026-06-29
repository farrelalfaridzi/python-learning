from core.character import Character

from core.item import Item

from core.weapon import Weapon

from core.player import Player

from core.monster import Monster

from core.inventory import Inventory

from core.potion import Potion

from core.armor import Armor

from game.battle import Battle

player = Player("Farrel", 100, 50, None, None)
wood = Weapon("Wood Sword",15,30)
small = Potion("small potion",10,10)
monster = Monster("Goblin",100,20,small,250)
leather = Armor("Leather armor",10,50)
battle = Battle(player, monster, small)

player.buy(leather)
player.equip_armor(leather)
player.buy(wood)
player.equip_weapon(wood)
battle.start()