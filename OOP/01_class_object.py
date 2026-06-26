class Monster:
    def __init__(self, nama, hp, damage):
        self.nama = nama
        self.hp = hp
        self.damage = damage

    def status(self):
        print("Nama :", self.nama)
        print("HP :", self.hp)
        print("Damage :", self.damage)

goblin = Monster("Goblin", 100, 15)

goblin.status()