class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def player_turn(self):
        while True:
            self.show_menu()
            pilih = input(">> ")
            if pilih == "1":
                self.handle_attack()
                break
            elif pilih == "2":
                self.handle_inventory()
            elif pilih == "3":
                self.handle_status()
            else:
                print("Pilihan tidak valid!")

    def monster_turn(self):
        self.monster.attack(self.player)

    def start(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player_turn()
            if self.check_monster_dead():
                break
            self.monster_turn()
            if self.check_player_dead():
                break
            self.show_hp()

    def show_hp(self):
        self.divider()
        print(f"{self.player.nama} HP : {self.player.hp}")
        print(f"{self.monster.nama} HP : {self.monster.hp}")
        self.divider()

    def show_menu(self):
        print("=== PLAYER TURN ===")
        print("1. Attack")
        print("2. Inventory")
        print("3. Status")
        self.divider()

    def show_inventory_menu(self):
        while True:
            if not self.player.inventory.items:
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
        self.divider()
        print("YOU WIN!")
        print(f"{self.monster.nama} menjatuhkan {self.monster.loot.nama}")
        self.player.inventory.add_item(self.monster.loot)
        self.player.gain_exp(self.monster.exp_reward)
        self.monster.defeated()
        self.divider()

    def check_monster_dead(self):
        if self.monster.hp <= 0:
            self.show_win()
            self.player.add_battle_won()
            self.player.add_monster_defeated()
            return True
        else:
            return False

    def check_player_dead(self):
        if self.player.hp <= 0:
            print("GAME OVER")
            self.player.defeated()
            self.player.add_battle_lost()
            return True
        else:
            return False

    def handle_attack(self):
        self.player.attack(self.monster)

    def handle_inventory(self):
        self.show_inventory_menu()

    def handle_status(self):
        self.player.status()
        self.monster.status()

    def divider(self):
        print("--------------------")