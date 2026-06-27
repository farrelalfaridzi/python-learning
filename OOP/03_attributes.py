class Player:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

player = Player("Farrel", 100)
print(player.nama)
print(player.hp)
player.nama  = "Budi"
player.hp -= 30
print(player.nama)
print(player.hp)