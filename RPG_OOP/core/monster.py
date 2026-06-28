from core.character import Character
class Monster(Character):
    def __init__(self, nama, hp, damage, loot):
        super().__init__(nama, hp)
        self.damage = damage
        self.loot = loot

    def status(self):
        print("=== MONSTER ===")
        super().status()
        print("Damage :", self.damage)

    def attack(self, player):
        print(f"{self.nama} menyerang balik!")
        player.take_damage(self.damage)

    def die(self, player):
        player.inventory.add_item(self.loot)