# Challenge 10 - Kasir Mini
# Dibuat oleh Farrel
#
# Materi:
# - Variabel
# - Input Output
# - If Else
# - While Loop
# - Operator Matematika (+)
# - int()

total = 0

while True :
    print("===Kasir Mini===")
    print("1. mie goreng : 3000")
    print("2. teh manis : 2000")
    print("3. batagor : 2000")
    print("4. bayar")
    print("================")

    pilih = input("aksi :")
    if pilih == "1":
        total += 3000
        print ("total :", total)
    elif pilih == "2":
        total += 2000
        print ("total :", total)
    elif pilih == "3":
        total += 2000
        print("total :", total)
    elif pilih == "4":
        print("total belanjaan :", total)
        print("terimakasih")
        break
    else :
        print("tidak valid")