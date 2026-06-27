class Character:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp =hp
        
    def status(self):
        print("=== STATUS ===")
        print("Nama :", self.nama)
        print("HP :", self.hp)

class Player(Character):
    def __init__(self, nama, hp):
        super().__init__(nama, hp)

    def status(self):
        super().status()
        print("Class : Player")

class Monster(Character):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp)
        self.damage = damage

    def status(self):
        super().status()
        print("==============")

player = Player("Farrel",100)
monster = Monster("Goblin", 100, 15)

player.status()
monster.status()