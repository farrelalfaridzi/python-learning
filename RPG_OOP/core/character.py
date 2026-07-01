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

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100