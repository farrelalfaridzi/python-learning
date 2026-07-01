class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def player_turn(self):
        while True:
            self.show_menu()
            pilih = input(">> ")
            if pilih == "1":
                self.player.attack(self.monster)
                break
            elif pilih == "2":
                self.show_inventory_menu()
            elif pilih == "3":
                self.player.status()
                self.monster.status()
            else:
                print("Pilihan tidak valid!")

    def monster_turn(self):
        self.monster.attack(self.player)

    def start(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player_turn()
            if self.monster.hp <= 0:
                self.show_win()
                break
            self.monster_turn()
            if self.player.hp <= 0:
                print("GAME OVER")
                self.player.defeated()
                break
            self.show_hp()

    def show_hp(self):
        print("---------------")
        print(f"{self.player.nama} HP : {self.player.hp}")
        print(f"{self.monster.nama} HP : {self.monster.hp}")
        print("---------------")

    def show_menu(self):
        print("=== PLAYER TURN ===")
        print("1. Attack")
        print("2. Inventory")
        print("3. Status")
        print("===================")

    def show_inventory_menu(self):
        while True:
            if len(self.player.inventory.items) == 0:
                print("tidak ada item")
                break
            else:
                self.open_inventory()
                nomor = int(input("Nomor item :"))
                if nomor > len(self.player.inventory.items) or nomor <0:
                    print("tidak valid")
                elif nomor == 0:
                    print("keluar inventory...")
                    break
                else:
                    item = self.player.inventory.choose_item(nomor)
                    if item is None:
                        print("pilihan tidak valid")
                        continue
                    item.use(self.player)

    def open_inventory(self):
        self.player.inventory.show_inventory()
        print("#tekan 0 untuk keluar shop")

    def show_win(self):
        print("--------------")
        print("YOU WIN!")
        print(f"{self.monster.nama} menjatuhkan {self.monster.loot.nama}")
        self.player.inventory.add_item(self.monster.loot)
        self.player.gain_exp(self.monster.exp_reward)
        self.monster.defeated()
        print("--------------")