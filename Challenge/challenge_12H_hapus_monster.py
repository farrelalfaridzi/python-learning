# Challenge 12H - Hapus Monster
# Dibuat oleh Farrel
#
# Materi:
# - List
# - Dictionary
# - For Loop
# - While Loop
# - If Else
# - Input Output
# - Boolean

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
    print("3. hapus monster")
    print("4. keluar")
    print("=============")
    pilih = input("Pilih aksi :")
    if pilih == "1":
        nama_monster = input("Nama :")
        monster["nama"] = nama_monster
        hp_monster = int(input("HP :"))
        monster["hp"] = hp_monster
        damage_monster = int(input("Damage :"))
        monster["damage"] = damage_monster
        daftar_monster.append(monster)
        print("monster berhasil ditambah")
        print(monster["nama"],"|","HP :",monster["hp"],"|","Damage :",monster["damage"])
    elif pilih == "2":
        if len(daftar_monster) == 0:
            print("tidak ada data")
        else :
            print("===DATA MONSTER===")
            for item in daftar_monster:
                print(item["nama"],"|","HP :",item["hp"],"|","Damage :",item["damage"])
            print("==================")
    elif pilih == "3":
        nama = input("Nama :")
        ditemukan = False
        for item in daftar_monster:
            if nama == item["nama"]:
                ditemukan = True
                daftar_monster.remove(item)
                print("monster dihapus")
        print("===DATA MONSTER===")
        for item in daftar_monster:
                print(item["nama"],"|","HP :",item["hp"],"|","Damage :",item["damage"])
        print("==================")
        if ditemukan == False:
            print("monster tidak ditemukan")
    elif pilih == "4":
        print("terimakasih...")
        break
    else:
        print("tidak valid")