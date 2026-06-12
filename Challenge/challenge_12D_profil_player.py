# Challenge 12D - Profil Player
# Dibuat oleh Farrel
#
# Materi:
# - Dictionary
# - While Loop
# - If Else
# - Operator Matematika
# - Input Output

player = {
    "nama" : "Farrel",
    "hp" : 100,
    "gold" : 50,
    "level" : 1
}

while True :
    print("===PLAYER===")
    print("1. lihat profil")
    print("2. dapat gold")
    print("3. naik level")
    print("4. keluar")
    print("=============")
    pilih = input("pilih aksi :")
    if pilih == "1":
        print("===PROFIL===")
        print("Nama :", player["nama"])
        print("HP :", player["hp"])
        print("Gold :", player["gold"])
        print("Level :", player["level"])
        print("=============")
    elif pilih == "2":
        jumlah_gold = int(input("jumlah gold :"))
        player["gold"] += jumlah_gold
        print("Gold :", player["gold"])
    elif pilih == "3":
        player["level"] += 1
        player["hp"] += 10
        print("Level :", player["level"])
        print("Hp :", player["hp"])
    elif pilih == "4":
        print("terima kasih...")
        break
    else :
        print("tidak valid")