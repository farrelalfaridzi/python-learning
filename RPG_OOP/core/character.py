class Character:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def status(self):
        print("Nama :", self.nama)
        print("HP :", self.hp)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"darah {self.nama} berkurang -{damage}")