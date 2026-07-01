class Character:
    def __init__(self, nama, hp):
        self._nama = nama
        self._hp = hp

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

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = value
        if self._hp > 100:
            self._hp = 100
        elif self._hp < 0:
            self._hp = 0

    @property
    def nama(self):
        return self._nama
    @nama.setter
    def nama(self, nama):
        self._nama = nama