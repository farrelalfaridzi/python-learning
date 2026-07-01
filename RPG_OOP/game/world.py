from game.battle import Battle

class World:
    def __init__(self,player,monsters,shop):
        self.player = player
        self.monsters = monsters
        self.shop = shop

    def show_menu(self):
        print("===== WORLD =====")
        print("1. Battle Goblin")
        print("2. Battle Orc")
        print("3. Battle Skeleton")
        print("4. Battle Dragon")
        print("5. Shop")
        print("6. Inventory")
        print("7. Status")
        print("0. Exit")

    def start(self):
        while True:
            self.show_menu()
            pilih = input(">> ")
            if pilih == "0":
                print("Exit...")
                break
            elif pilih == "1":
                battle = Battle(self.player,self.monsters[0])
                battle.start()
            elif pilih == "2":
                battle2 = Battle(self.player,self.monsters[1])
                battle2.start()
            elif pilih == "3":
                battle3 = Battle(self.player,self.monsters[2])
                battle3.start()
            elif pilih == "4":
                battle4 = Battle(self.player,self.monsters[3])
                battle4.start()
            elif pilih == "5":
                self.shop.open(self.player)
            elif pilih == "6":
                self.player.inventory.show_inventory()
            elif pilih == "7":
                self.player.status()