import json
class SaveManager:
    def save(self, player):
        data = {
            "nama":player.nama,
            "hp":player.hp,
            "gold":player.gold,
            "level":player.level,
            "exp":player.exp,
            "bonus_damage":player.bonus_damage,
            "weapon":player.weapon.nama if player.weapon else None,
            "armor":player.armor.nama if player.armor else None,
            "monster_defeated":player.monster_defeated,
            "battle_won":player.battle_won,
            "battle_lost":player.battle_lost,
            "damage_taken":player.damage_taken,
            "damage_dealt":player.damage_dealt,
            "potion_used":player.potion_used
        }
        with open("save.json","w") as file:
            json.dump(data,file)
        print("Data berhasil disimpan")

    def load(self,player):
        with open("save.json","r") as file:
            data = json.load(file)
            player.nama = data["nama"]
            player.hp = data["hp"]
            player.gold = data["gold"]
            player.level = data["level"]
            player.exp = data["exp"]
            player.bonus_damage = data["bonus_damage"]
            player.monster_defeated = data["monster_defeated"]
            player.battle_won = data["battle_won"]
            player.battle_lost = data["battle_lost"]
            player.damage_taken = data["damage_taken"]
            player.damage_dealt = data["damage_dealt"]
            player.potion_used = data["potion_used"]
            print("Data berhasil dimuat")