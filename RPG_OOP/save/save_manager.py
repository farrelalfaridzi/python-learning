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
            "armor":player.armor.nama if player.armor else None
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
            print("Data berhasil dimuat")