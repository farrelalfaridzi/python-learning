# RPG V4
# Dibuat oleh Farrel
#
# Materi:
# - Dictionary
# - List
# - Function
# - Random
# - While Loop
# - If Else
# - Boolean

inventory = []
daftar_monster = []
loot_random = [
    "super potion",
    "elixir",
    "potion"
]
player = {
    "nama" : "Farrel",
    "hp" : 100,
    "max_hp" : 100,
    "gold" : 50,
    "level" : 1,
    "exp" : 0
}
nama_random_monster = [
    "Goblin",
    "Orc",
    "Dragon",
    "Slime",
    "Skeleton"
]

monster_aktif = None

import random
def attack():
    return random.randint(20, 30)
def heal():
    return random.randint(10, 20)
def status(player, monster_aktif):
    print("===STATUS===")
    print("Nama :", player["nama"])
    print("HP :", player["hp"])
    print("Gold :", player["gold"])
    print("Level :", player["level"])
    print("EXP :", player["exp"])
    print("Monster :", monster_aktif["nama"])
    print("HP Monster :", monster_aktif["hp"])
    print("============")
def spawn_monster():
    monster_random = {
            "nama" : random.choice(nama_random_monster),
            "hp" : random.randint(50, 100),
            "damage" : random.randint(5, 20)
        }
    return monster_random

while True:
    print("===ACTION===")
    print("1. attack")
    print("2. heal")
    print("3. inventory")
    print("4. status")
    print("5. shop")
    print("6. tambah monster")
    print("7. lihat monster")
    print("8. pilih monster")
    print("9. spawn monster")
    print("10. keluar")
    print("============")
    pilih = input("pilihan :")
    if pilih == "4":
        if monster_aktif == None:
            print("silahkan pilih monster terlebih dahulu")
        else :
            status(player, monster_aktif)
    elif pilih == "10":
        print("terimakasih...")
        break
    elif pilih == "2":
        player["hp"] += heal()
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        print("player berhasil di heal")
        print("HP :", player["hp"])
    elif pilih == "1":
        if monster_aktif == None:
            print("silahkan pilih monster terlebih dahulu")
        else :
            damage = attack()
            print("Damage :", damage)
            monster_aktif["hp"] -= damage
            if monster_aktif["hp"] < 0:
                monster_aktif["hp"] = 0
            print("HP", monster_aktif["nama"],":",monster_aktif["hp"])
            if monster_aktif["hp"] <= 0:
                print("YOU WIN!")
                monster_kalah_loot = random.choice(loot_random)
                inventory.append(monster_kalah_loot)
                print("kamu mendapatkan",monster_kalah_loot)
                player["gold"] += 15
                print("Gold :", player["gold"])
                player["exp"] += 10
                print("EXP :", player["exp"])
                if player["exp"] >= 30:
                    player["level"] += 1
                    player["exp"] -= 30
                    player["max_hp"] += 30
                    player["hp"] = player["max_hp"]
                    print("Level up")
                    print("player berhasil dipulihkan")
                    print("level :", player["level"])
                    print("Max HP :", player["max_hp"])
                daftar_monster.remove(monster_aktif)
                monster_aktif = None
                continue
            #monster
            print("monster menyerang balik")
            player["hp"] -= monster_aktif["damage"]
            print("Damage monster :", monster_aktif["damage"])
            if player["hp"] <= 0:
                print("Game over")
                break
    elif pilih == "3":
        if len(inventory) == 0:
            print("iventory kosong")
        else :
            while True:
                print("===INVENTORY===")
                print("1. lihat inventory")
                print("2. pakai item")
                print("3. keluar")
                print("===============")
                pilih_item = input("pilih :")
                if pilih_item == "2":
                    nama_item = input("nama item :")
                    if nama_item in inventory:
                        inventory.remove(nama_item)
                        print("item berhasil digunakan")
                        if nama_item == "potion":
                            player["hp"] += 10
                            if player["hp"] > player["max_hp"]:
                                player["hp"] = player["max_hp"]
                            print("HP :", player["hp"])
                        elif nama_item == "elixir":
                            player["exp"] += 10
                            print("exp :",player["exp"])
                        elif nama_item == "super potion":
                            player["hp"] += 30
                            if player["hp"] > player["max_hp"]:
                                player["hp"] = player["max_hp"]
                            print("HP :", player["hp"])
                    else :
                        print("item tidak ada di tas")
                elif pilih_item == "3":
                    print("keluar inventory")
                    break
                elif pilih_item == "1":
                    if len(inventory) == 0:
                        print("tidak ada item")
                    else:
                        for item in inventory:
                            print(item)
    elif pilih == "5":
        while True:
            print("===SHOP===")
            print("1. potion(10 gold)")
            print("2. keluar")
            print("==========")
            pilih_shop = input("beli :")
            if pilih_shop == "1":
                if player["gold"] >= 10:
                    player["gold"] -= 10
                    inventory.append("potion")
                    print("item berhasil ditambah")
                    print("Gold :", player["gold"])
                else :
                    print("gold tidak cukup")
            elif pilih_shop == "2":
                print("keluar shop...")
                break
    elif pilih == "6":
        monster = {
            "nama" : "",
            "hp" : 0,
            "damage" : 0
        }
        nama_monster = input("Nama :")
        monster["nama"] = nama_monster
        hp_monster = int(input("HP monster :"))
        monster["hp"] = hp_monster
        damage_monster = int(input("Damage monster :"))
        monster["damage"] = damage_monster
        daftar_monster.append(monster)
        print("monster berhasil ditambah")
        print(monster["nama"],"|","HP :", monster["hp"],"|","Damage :",monster["damage"])
    elif pilih == "7":
        if len(daftar_monster) == 0:
            print("tidak ada monster")
        else:
            for item in daftar_monster:
                print(item["nama"],"|","HP :",item["hp"],"|","Damage",item["damage"])
    elif pilih == "8":
        if len(daftar_monster) == 0:
            print("silahkan tambah monster terlebih dahulu")
        else:
            nomor = 0
            print("===PILIH MONSTER===")
            for item in daftar_monster:
                nomor += 1
                print(nomor, item["nama"])
            print("===================")
            pilih_monster = int(input("pilih angka monster :"))
            if pilih_monster > len(daftar_monster) or pilih_monster < 1:
                print("angka tidak valid")
            else:
                pilih_monster -= 1
                print("monster dipilih :")
                print(daftar_monster[pilih_monster]["nama"])
                print("HP :",daftar_monster[pilih_monster]["hp"])
                print("Damage :",daftar_monster[pilih_monster]["damage"])
                monster_aktif = daftar_monster[pilih_monster]
    elif pilih == "9":
        monster_baru = spawn_monster
        print("monster dibuat")
        print(monster_baru["nama"],"|","HP :", monster_baru["hp"],"|","Damage :", monster_baru["damage"])
        daftar_monster.append(monster_baru)
    else:
        print("tidak valid")