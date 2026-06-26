# RPG V7
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
# - Git & GitHub
# - File Handling 
#
# Fitur:
# - Battle System
# - Inventory
# - Shop
# - Level & EXP
# - Loot System
# - Random Monster Spawn
# - Save & Load Game (WIP)
# - Quest
# - Equipment sytem

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
    "exp" : 0,
    "weapon_aktif" : None
}
quest = {
    "nama_quest" : "bunuh 3 monster",
    "progress" : 0,
    "target" : 3,
    "reward" : 50,
    "quest_done" : False
}
nama_random_monster = [
    "Goblin",
    "Orc",
    "Dragon",
    "Slime",
    "Skeleton"
]
daftar_weapon = [
    {
        "nama" : "pedang kayu",
        "damage" : 5,
        "harga" : 10,
        "level_minimum" : 1,
        "rarity" : "common"
    },
    {
        "nama" : "pedang besi",
        "damage" : 10,
        "harga" : 35,
        "level_minimum" : 2,
        "rarity" : "uncommon"
    },
    {
        "nama" : "pedang naga",
        "damage" : 15,
        "harga" : 55,
        "level_minimum" : 4,
        "rarity" : "epic"
    }
]

monster_aktif = None

import random
def attack(player):
    damage_random = random.randint(20, 30)
    bonus_damage = 0
    if player["weapon_aktif"] != None:
        bonus_damage = player["weapon_aktif"]["damage"]
    damage_total = damage_random + bonus_damage
    return damage_total
def heal():
    return random.randint(10, 20)
def status(player, monster_aktif):
    print("===STATUS===")
    print("Nama :", player["nama"])
    print("HP :", player["hp"])
    print("Gold :", player["gold"])
    print("Level :", player["level"])
    print("EXP :", player["exp"])
    if player["weapon_aktif"] == None:
        print("weapon : tangan kosong")
        print("Damage bonus : 0")
    else :
        print("weapon :", player["weapon_aktif"]["nama"])
        print("Damage bonus :","+",player["weapon_aktif"]["damage"])
    print("============")
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
def shop(player, inventory, daftar_weapon):
    while True:
            print("===SHOP===")
            print("1. potion(10 gold)")
            print("2. keluar")
            print("3. weapon")
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
            elif pilih_shop == "3":
                no = 0
                print("===WEAPON===")
                for x in daftar_weapon :
                    no += 1
                    print(no, x["nama"],"|","harga :",x["harga"],"|","level min :",x["level_minimum"])
                print("============")
                beli_weapon = int(input("pilih no weapon :"))
                if beli_weapon > len(daftar_weapon) or beli_weapon<1:
                    print("tidak valid")
                else :
                    beli_weapon -= 1
                    if player["gold"] >= daftar_weapon[beli_weapon]["harga"]:
                        player["gold"] -= daftar_weapon[beli_weapon]["harga"]
                        print("weapon yang dibeli :")
                        print(daftar_weapon[beli_weapon]["nama"],"|","damage :",daftar_weapon[beli_weapon]["damage"],"|","rarity :",daftar_weapon[beli_weapon]["rarity"])
                        inventory.append(daftar_weapon[beli_weapon])
                        print("item berhasil dibeli")
                        print("gold :",player["gold"])
                    else:
                        print("gold tidak cukup")
def inventory_menu(player, inventory):
    while True:
                if len(inventory) == 0:
                    print("tas kosong")
                    return
                print("===INVENTORY===")
                print("1. lihat inventory")
                print("2. pakai item")
                print("3. keluar")
                print("===============")
                pilih_item = input("pilih :")
                if pilih_item == "2":
                    nama_item = input("nama item :")
                    item_ketemu = False
                    for item in inventory:
                        if isinstance(item, str):
                            if nama_item == item:
                                item_ketemu = True
                                inventory.remove(nama_item)
                                print("item berhasil digunakan")
                                if nama_item == "potion":
                                    player["hp"] += 10
                                    if player["hp"] > player["max_hp"]:
                                        player["hp"] = player["max_hp"]
                                    print("HP :", player["hp"])
                                    break
                                elif nama_item == "elixir":
                                    player["exp"] += 10
                                    print("exp :",player["exp"])
                                    break
                                elif nama_item == "super potion":
                                    player["hp"] += 30
                                    if player["hp"] > player["max_hp"]:
                                        player["hp"] = player["max_hp"]
                                    print("HP :", player["hp"])
                                    break
                        elif isinstance(item, dict) :
                            if nama_item == item["nama"]:
                                item_ketemu = True
                                player["weapon_aktif"] = item
                                print("damage bonus :", item["damage"])
                                break
                    if item_ketemu == False :
                        print("item tidak ada di inventory")
                elif pilih_item == "3":
                    print("keluar inventory")
                    break
                elif pilih_item == "1":
                    if len(inventory) == 0:
                        print("tidak ada item")
                    else:
                        for item in inventory:
                            if type(item) is str:
                                print(item)
                            else:
                                if player["weapon_aktif"] == None:
                                    print(item["nama"])
                                else:
                                    if player["weapon_aktif"]["nama"] == item["nama"]:
                                        print(item["nama"] + "[EQUIPPED]")
                                    else :
                                        print(item["nama"])
def attack_menu(player, monster_aktif, daftar_monster, inventory, quest, daftar_weapon):
    damage = attack(player)
    print("Damage :", damage)
    monster_aktif["hp"] -= damage
    if monster_aktif["hp"] < 0:
        monster_aktif["hp"] = 0
    print("HP", monster_aktif["nama"],":",monster_aktif["hp"])
    if monster_aktif["hp"] <= 0:
        print("YOU WIN!")
        quest["progress"] += 1
        if quest["progress"] >= quest["target"] and quest["quest_done"] == False:
            player["gold"] += quest["reward"]
            quest["quest_done"] = True
            print("quest selesai!")
            print("+", quest["reward"], "gold")
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
        drop_chance = random.randint(1, 100)
        if drop_chance <= 50:
            weapon_drop = random.choice(daftar_weapon)
            weapon_sudah_ada = False
            for item in inventory:
                if isinstance(item, dict):
                    if item["nama"] == weapon_drop["nama"]:
                        weapon_sudah_ada = True
                        break
            if weapon_sudah_ada == False:
                inventory.append(weapon_drop)
                print("=============")
                print("weapon drop!")
                print(weapon_drop["nama"])
                print("damage :", weapon_drop["damage"])
                print("rarity :", weapon_drop["rarity"])
                print("=============")
            else:
                print("weapon sudah dimiliki")
        daftar_monster.remove(monster_aktif)
        monster_aktif = None
        return monster_aktif
    #monster
    print("monster menyerang balik")
    player["hp"] -= monster_aktif["damage"]
    print("Damage monster :", monster_aktif["damage"])
    if player["hp"] <= 0:
        print("Game over")
        return monster_aktif
    return monster_aktif
def save_game(player, inventory):
    file = open("save.txt", "w")
    list_sementara = []
    for item in inventory :
        if isinstance(item, str) :
            list_sementara.append(item)
        else :
            list_sementara.append(item["nama"])
    gabung = ",".join(list_sementara)
    file.write("nama=" + player["nama"] + "\n")
    file.write("hp=" + str(player["hp"]) + "\n")
    file.write("gold=" + str(player["gold"]) + "\n")
    file.write("max_hp=" + str(player["max_hp"]) + "\n")
    file.write("level=" + str(player["level"]) + "\n")
    file.write("exp=" + str(player["exp"]) + "\n")
    if player["weapon_aktif"] == None:
        file.write("weapon=" + "None" + "\n")
    elif player["weapon_aktif"] != None:
        file.write("weapon=" + player["weapon_aktif"]["nama"] + "\n")
    file.write("inventory=" + gabung)
    file.close()
def load_game(player, daftar_weapon, inventory):
    file = open("save.txt", "r")
    data = file.read()
    baris = data.split("\n")
    player["nama"] = baris[0].split("=")[1]
    player["hp"] = int(baris[1].split("=")[1])
    player["gold"] = int(baris[2].split("=")[1])
    player["max_hp"] = int(baris[3].split("=")[1])
    player["level"] = int(baris[4].split("=")[1])
    player["exp"] = int(baris[5].split("=")[1])
    if baris[6].split("=")[1] == "None":
        player["weapon_aktif"] = None
    else :
        weapon_ketemu = False
        for weapon in daftar_weapon:
            if weapon["nama"] == baris[6].split("=")[1]:
                weapon_ketemu = True
                player["weapon_aktif"] = weapon
        if weapon_ketemu == False:
            print("weapon tidak ada")
            player["weapon_aktif"] = None
    inventory = baris[7].split("=")[1].split(",")
    file.close()

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
    print("11. save game")
    print("12. load game")
    print("13. lihat quest")
    print("14. lihat weapon")
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
            monster_aktif = attack_menu(player, monster_aktif, daftar_monster, inventory, quest, daftar_weapon)
    elif pilih == "3":
        if len(inventory) == 0:
            print("iventory kosong")
        else :
            inventory_menu(player, inventory)
    elif pilih == "5":
        shop(player, inventory, daftar_weapon)
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
        monster_baru = spawn_monster()
        print("monster dibuat")
        print(monster_baru["nama"],"|","HP :", monster_baru["hp"],"|","Damage :", monster_baru["damage"])
        daftar_monster.append(monster_baru)
    elif pilih == "11":
        save_game(player, inventory)
        print("player berhasil di save")
    elif pilih == "12":
        load_game(player, daftar_weapon)
        print("===GAME BERHASIL DIMUAT===")
    elif pilih == "13":
        if quest["quest_done"] == False:
            print("nama quest :", quest["nama_quest"])
            print("progress :", quest["progress"])
            print("target :", quest["target"])
            print("reward :", quest["reward"])
        elif quest["quest_done"] == True:
            print("quest telah selesai")
    elif pilih == "14":
        for x in daftar_weapon:
            print(x["nama"],"|","Damage bonus :",x["damage"],"|","level min :",x["level_minimum"],"|","rarity :",x["rarity"])
    else:
        print("tidak valid")