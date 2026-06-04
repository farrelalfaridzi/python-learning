#inventory
tas = []

while True:
    print ("===INVENTORY===")
    print ("1. lihat tas")
    print ("2. ambil item")
    print ("3. hapus item")
    print ("4. tutup")
    print ("===============")

    pilih = input("PILIHAN :")
    if pilih == "1":
        if len(tas) == 0 :
            print ("TAS KOSONG")
        for item in tas :
            print (item)
    elif pilih == "2":
        item = input("ITEM :")
        tas.append(item)
        print(tas)
    elif pilih == "3":
        print (tas)
        buang = input("ITEM :")
        if buang in tas:
            tas.remove(buang)
            print(tas)
        else :
            print("item tidak ada")
    elif pilih == "4":
        print("keluar...")
        break