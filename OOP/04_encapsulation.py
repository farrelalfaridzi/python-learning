class Player:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def status(self):
        print("=== STATUS ===")
        print("Nama :", self.nama)
        print("HP :", self.hp)

player = Player("Farrel", 100)
player.take_damage(500)
player.status()
