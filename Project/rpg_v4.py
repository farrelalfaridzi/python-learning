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
player = {
    "nama" : "Farrel",
    "hp" : 100,
    "gold" : 50,
    "level" : 1,
    "exp" : 0
}
monster = {
    "nama" : "Goblin",
    "hp" : 50,
    "damage" : 10
}
import random
def attack():
    return random.randint(20, 30)
def heal():
    return random.randint(10, 20)
def status(player, monster):
    print("===STATUS===")
    print("Nama :", player["nama"])
    print("HP :", player["hp"])
    print("Gold :", player["gold"])
    print("Level :", player["level"])
    print("EXP :", player["exp"])
    print("Monster :", monster["nama"])
    print("HP Monster :", monster["hp"])
    print("============")

while player["hp"] > 0 and monster["hp"] > 0:
    print("===ACTION===")
    print("1. attack")
    print("2. heal")
    print("3. inventory")
    print("4. status")
    print("5. shop")
    print("6. keluar")
    print("============")
    pilih = input("pilihan :")
    if pilih == "4":
        status(player, monster)
    elif pilih == "6":
        print("terimakasih...")
        break
    elif pilih == "2":
        player["hp"] += heal()
        print("player berhasil di heal")
        print("HP :", player["hp"])
    elif pilih == "1":
        damage = attack()
        print("Damage :", damage)
        monster["hp"] -= damage
        print("HP", monster["nama"],":",monster["hp"])
        if monster["hp"] <= 0:
            print("YOU WIN!")
            break
        #monster
        print("monster menyerang balik")
        player["hp"] -= monster["damage"]
        print("Damage monster :", monster["damage"])
        if player["hp"] <= 0:
            print("Game over")
            break
        player["gold"] += 15
        print("Gold :", player["gold"])
        player["exp"] += 10
        print("EXP :", player["exp"])
        if player["exp"] >= 30:
            player["level"] += 1
            player["exp"] -= 30
            print("Level up")
            print("level :", player["level"])
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