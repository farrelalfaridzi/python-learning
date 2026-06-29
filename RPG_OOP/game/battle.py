class Battle:
    def __init__(self, player, monster, potion):
        self.player = player
        self.monster = monster
        self.potion = potion

    def player_turn(self):
        while True:
            self.show_menu()
            pilih = input(">> ")
            if pilih == "1":
                self.player.attack(self.monster)
                break
            elif pilih == "2":
                self.player.drink(self.potion)
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
                print("YOU WIN!")
                print(f"{self.monster.nama} menjatuhkan {self.monster.loot.nama}")
                self.player.inventory.add_item(self.monster.loot)
                self.player.gain_exp(self.monster.exp_reward)
                break
            self.monster_turn()
            if self.player.hp <= 0:
                print("GAME OVER")
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
        print("2. Drink potion")
        print("3. Status")
        print("===================")