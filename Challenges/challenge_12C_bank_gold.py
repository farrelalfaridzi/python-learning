# Challenge 12C - Profil Karakter
# Dibuat oleh Farrel
#
# Materi:
# - Dictionary
# - While Loop
# - If Else
# - Operator Matematika
# - Input Output

bank = {
    "gold" : 0
}

while True:
    print("===BANK GOLD===")
    print("1. lihat gold")
    print("2. setor gold")
    print("3. tarik gold")
    print("4. keluar")
    print("===============")
    player = input("pilih :")
    if player == "1":
        print("Gold :", bank["gold"])
    elif player == "2":
        setor = int(input("jumlah setor :"))
        bank["gold"] += setor
        print("Gold :", bank["gold"])
    elif player == "3":
        tarik = int(input("jumlah tarik :"))
        if tarik <= bank["gold"]:
            bank["gold"] -= tarik
            print("Gold :", bank["gold"])
        else :
            print("saldo tidak cukup")
    elif player == "4":
        print("terima kasih...")
        break
    else :
        print("tidak valid")