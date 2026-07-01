from core.character import Character
class Monster(Character):
    def __init__(self, nama, hp, damage, loot, exp_reward):
        super().__init__(nama, hp)
        self._damage = damage
        self._loot = loot
        self._exp_reward = exp_reward
        self.is_defeated = False

    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, value):
        self._damage = value
        if self._damage < 0:
            self._damage = 0

    @property
    def loot(self):
        return self._loot
    @loot.setter
    def loot(self, loot):
        self._loot = loot

    @property
    def exp_reward(self):
        return self._exp_reward
    @exp_reward.setter
    def exp_reward(self, value):
        self._exp_reward = value

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
        player.add_damage_taken(damage_diterima)

    def defeated(self):
        self.is_defeated = True