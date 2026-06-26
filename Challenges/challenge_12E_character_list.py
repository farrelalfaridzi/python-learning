# Challenge 12E - Daftar Karakter
# Dibuat oleh Farrel
#
# Materi:
# - List
# - Dictionary
# - For Loop
# - While Loop
# - If Else
# - Input Output

daftar_player = [

]


while True :
    player = {
    "nama" : "",
    "job" : ""
}
    print("===KARAKTER===")
    print("1. tambahkan karakter")
    print("2. lihat karakter")
    print("3. keluar")
    print("==============")
    pilih = input("pilih aksi :")
    if pilih == "1":
        nama = input("Nama :")
        player["nama"] = nama
        job = input("Job :")
        player["job"] = job
        daftar_player.append(player)
        print(player["nama"], "-", player["job"])
    elif pilih == "2":
        if len(daftar_player) == 0:
            print("Tidak ada karakter")
        else :
            print("===DAFTAR KARAKTER===")
            for item in daftar_player:
                print(item["nama"], "-", item["job"])
            print("=====================")
    elif pilih == "3":
        print("terimakasih...")
        break
    else :
        print("tidak valid")