class World:
    def __init__(self,player,monsters,shop):
        self.player = player
        self.monsters_menu = monsters
        self.shop = shop

    def show_menu(self):
        print("===== WORLD =====")
        print("1. Choose monster")
        print("2. Shop")
        print("3. Inventory")
        print("4. Status")
        print("0. Exit")

    def start(self):
        while True:
            if self.player.is_defeated == True:
                break
            self.show_menu()
            pilih = input(">> ")
            if pilih == "0":
                print("Exit...")
                break
            elif pilih == "1":
                self.monsters_menu.open(self.player)
            elif pilih == "2":
                self.shop.open(self.player)
            elif pilih == "3":
                self.player.inventory.show_inventory()
            elif pilih == "4":
                self.player.status()
            else:
                print("input tidak valid")
            check_monster = self.monsters_menu.check_all_monsters()
            if check_monster is True:
                print("----- CONGRATULATIONS -----")
                print("-you defeated all monsters-")
                print("---------------------------")
                break