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

from save.save_manager import SaveManager

class Game:
    def __init__(self):
        self.player = Player("Farrel",100)
        self.wood = Weapon("Wood Sword",15,30)
        self.bow = Weapon("Regular bow",20,50)
        self.small = Potion("small potion",10,10)
        self.leather = Armor("Leather armor",10,20)
        self.iron = Armor("Iron armor",30,50)
        self.goblin = Monster("Goblin",100,20,self.small,250)
        self.orc = Monster("Orc",180,30,self.leather,180)
        self.skeleton = Monster("Skeleton",250,40,self.bow,250)
        self.dragon = Monster("Dragon",500,70,self.iron,700)
        self.monster = Monsters_menu(self)
        self.monster.add_monster(self.goblin)
        self.monster.add_monster(self.orc)
        self.monster.add_monster(self.skeleton)
        self.monster.add_monster(self.dragon)
        self.shop = Shop()
        self.shop.add_item(self.wood)
        self.shop.add_item(self.bow)
        self.shop.add_item(self.small)
        self.shop.add_item(self.leather)
        self.shop.add_item(self.iron)
        self.save = SaveManager()
        self.world = World(self.player,self.monster,self.shop,self.save)

    def start(self):
        self.world.start()

    def start_battle(self, monster):
        battle = Battle(self.player,monster)
        battle.start()