from core.character import Character
class Monster(Character):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp)
        self.damage = damage

    def status(self):
        print("=== MONSTER ===")
        super().status()
        print("Damage :", self.damage)

    def attack(self, player):
        player.take_damage(self.damage)
        print(f"{self.nama} menyerang balik!")