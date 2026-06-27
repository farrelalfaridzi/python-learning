class Player:
    def __init__(self, nama, hp=100, gold=0, damage=10):
        self.nama = nama
        self.hp = hp
        self.gold = gold
        self.damage = damage

    def status(self):
        print("=== STATUS ===")
        print("Nama :", self.nama)
        print("HP : ", self.hp)
        print("Gold :", self.gold)
        print("Damage :", self.damage)
        print("==============")

player1 = Player("Farrel")
player2 = Player("Budi", 200)
player3 = Player("Aceng", 300, 50, 25)

player1.status()
player2.status()
player3.status()
