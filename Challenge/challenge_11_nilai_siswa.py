# Challenge 11 - Data Nilai Siswa
# Dibuat oleh Farrel
#
# Materi:
# - List
# - For Loop
# - While Loop
# - If Else
# - len()
# - max()
# - min()
# - int()

nilai = []

while True :
    print("==DATA NILAI SISWA==")
    print("1. tambah nilai")
    print("2. lihat semua nilai")
    print("3. nilai tertinggi")
    print("4. nilai terendah")
    print("5. keluar")
    print("====================")

    pilih = input("pilih :")
    if pilih == "1":
        item = int(input("masukan nilai :"))
        nilai.append(item)
    elif pilih == "2":
        for item in nilai:
            print(item)
    elif pilih == "3":
        if len(nilai) > 0 :
            print(max(nilai))
        elif len(nilai) == 0 :
            print("tidak ada data")
    elif pilih== "4":
        if len(nilai) > 0:
            print(min(nilai))
        elif len(nilai) == 0:
            print("tidak ada data")
    elif pilih == "5":
        print("terima kasih")
        break
    else :
        print("tidak valid ,ulangi")