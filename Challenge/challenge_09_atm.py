# Challenge 09 - ATM Mini
# Dibuat oleh Farrel

# Materi:
# - Variabel
# - Input Output
# - If Else
# - While Loop
# - Operator Matematika (+, -)
# - int()

saldo = 100000

while True:
    print("===ATM MINI===")
    print("1. cek saldo")
    print("2. setor tunai")
    print("3. ambil uang")
    print("4. keluar")
    print("==============")

    pilih = input("pilih :")
    if pilih == "1":
        print("saldo :", saldo)
    elif pilih == "2":
        setor = int(input("Jumlah Setor:"))
        saldo += setor
        print("saldo :", saldo)
    elif pilih == "3":
        tarik = int(input("Jumlah tarik:"))
        if tarik <= saldo:
            saldo -= tarik
            print("Berhasil")
            print("saldo :", saldo)
        elif tarik >= saldo:
            print("saldo tidak cukup")
    elif pilih == "4":
        print("terima kasih")
        break
    else :
        print("tidak valid")