# Challenge 12F - Data Monster
# Dibuat oleh Farrel
#
# Materi:
# - List
# - Dictionary
# - For Loop
# - While Loop
# - If Else
# - Input Output
# - int()

data_monster = [

]

while True:
    monster = {
        "nama" : "",
        "hp" : 0,
        "damage" : 0
    }
    print("===MONSTER===")
    print("1. tambah monster")
    print("2. lihat monster")
    print("3. keluar")
    print("=============")
    pilih = input("pilih aksi :")
    if pilih == "1":
        nama = input("Nama :")
        monster["nama"] = nama
        hp = int(input("HP :"))
        monster["hp"] = hp
        damage = int(input("Damage :"))
        monster["damage"] = damage
        data_monster.append(monster)
        print(monster["nama"], "|", "HP:", monster["hp"], "|", "Damage:", monster["damage"])
    elif pilih == "2":
        if len(data_monster) == 0:
            print("Tidak ada data")
        else :
            print("===DATA MONSTER===")
            for item in data_monster:
                print(item["nama"], "|", "HP:", item["hp"], "|", "Damage:", item["damage"])
            print("==================")
    elif pilih == "3":
        print("terimakasih...")
        break
    else:
        print("Tidak valid")