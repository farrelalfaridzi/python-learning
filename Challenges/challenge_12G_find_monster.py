# Challenge 12G - Cari Monster
# Dibuat oleh Farrel
#
# Materi:
# - List
# - Dictionary
# - For Loop
# - While Loop
# - If Else
# - Input Output

daftar_monster = [

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
    print("3. cari monster")
    print("4. keluar")
    print("=============")
    pilih = input("pilih aksi :")
    if pilih == "1":
        nama_monster = input("Nama :")
        monster["nama"] = nama_monster
        hp_monster = int(input("HP :"))
        monster["hp"] = hp_monster
        damage_monster = int(input("Damage :"))
        monster["damage"] = damage_monster
        daftar_monster.append(monster)
        print(monster["nama"], "|", "HP :", monster["hp"], "|", "Damage :", monster["damage"])
        print("Berhasil ditambahkan")
    elif pilih == "2":
        if len(daftar_monster) == 0:
            print("Tidak ada data")
        else :
            print("===DATA MONSTER===")
            for item in daftar_monster:
                print(item["nama"], "|", "HP :", item["hp"], "|", "Damage :", item["damage"])
            print("==================")
    elif pilih == "3":
        nama = input("Nama monster :")
        ditemukan = False
        for item in daftar_monster:
            if nama == item["nama"]:
                ditemukan = True
                print("Monster ditemukan")
                print(item["nama"])
                print("HP :", item["hp"])
                print("Damage :", item["damage"])
        if ditemukan == False:
            print("monster tidak ditemukan")
    elif pilih == "4":
        print("Terimakasih...")
        break
    else :
        print("tidak valid")