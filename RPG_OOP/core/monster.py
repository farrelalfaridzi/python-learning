from core.character import Character
class Monster(Character):
    def __init__(self, nama, hp, damage, loot, exp_reward):
        super().__init__(nama, hp)
        self.damage = damage
        self.loot = loot
        self.exp_reward = exp_reward

    def status(self):
        print("=== MONSTER ===")
        super().status()
        print("Damage :", self.damage)

    def attack(self, player):
        print(f"{self.nama} menyerang balik!")
        damage_diterima = self.damage
        if player.armor != None:
            damage_diterima -= player.armor.defense
            if damage_diterima <= 0:
                damage_diterima = 0
        player.take_damage(damage_diterima)