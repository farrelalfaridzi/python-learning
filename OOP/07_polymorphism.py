class Character:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def status(self):
        print("Nama :", self.nama)
        print("HP :", self.hp)
        print("==============")

class Player(Character):
    def __init__(self, nama, hp):
        super().__init__(nama, hp)

    def status(self):
        print("=== PLAYER ===")
        super().status()

class Monster(Character):
    def __init__(self, nama, hp):
        super().__init__(nama, hp)

    def status(self):
        print("=== MONSTER ===")
        super().status()

player = Player("Farrel", 100)
monster = Monster("Goblin", 100)

characters = [
    player,
    monster
]

for character in characters:
    character.status()
