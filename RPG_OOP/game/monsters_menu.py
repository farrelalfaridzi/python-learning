class Monsters_menu:
    def __init__(self, game):
        self.monsters = []
        self.game = game

    def add_monster(self, monster):
        self.monsters.append(monster)

    def show_menu(self):
        nomor = 0
        print("===== MONSTER =====")
        for monster in self.monsters:
            nomor += 1
            if monster.is_defeated == False:
                print(f"{nomor}. {monster.nama} (HP {monster.hp})")
            else:
                print(f"{nomor}. {monster.nama} (Defeated)")
        print("===================")

    def choose_monster(self, index):
        index -= 1
        if index >= len(self.monsters) or index < 0:
            print("pilihan tidak valid")
            return None
        else:
            return self.monsters[index]

    def open(self, player):
        while True:
            if player.is_defeated == True:
                break
            self.show_menu()
            print("#pilih 0 untuk keluar")
            pilih = int(input(">> "))
            if pilih == 0:
                print("keluar...")
                break
            else:
                monster = self.choose_monster(pilih)
                if monster is None:
                    print("pilihan tidak valid")
                self.game.start_battle(monster)
                if monster.is_defeated == True:
                    print(f"{monster.nama} sudah dikalahkan")

    def check_all_monsters(self):
        for monster in self.monsters:
            if monster.is_defeated == False:
                return False
        return True