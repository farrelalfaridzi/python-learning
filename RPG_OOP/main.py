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

from game.world import World

from game.monsters_menu import Monsters_menu

player = Player("Farrel", 100, 50, None, None)
wood = Weapon("Wood Sword",15,30)
bow = Weapon("Weapon",20,50)
small = Potion("small potion",10,10)
leather = Armor("Leather armor",10,20)
iron = Armor("Iron armor",30,50)
goblin = Monster("Goblin",100,20,small,250)
orc = Monster("Orc",180,30,leather,180)
skeleton = Monster("Skeleton",250,40,bow,250)
dragon = Monster("Dragon",500,70,iron,700)

monster = Monsters_menu()
monster.add_monster(goblin)
monster.add_monster(orc)
monster.add_monster(skeleton)
monster.add_monster(dragon)

shop = Shop()
shop.add_item(wood)
shop.add_item(small)
shop.add_item(leather)
world = World(player,monster,shop)
world.start()