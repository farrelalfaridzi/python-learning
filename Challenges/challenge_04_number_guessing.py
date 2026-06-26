import random
angka = random.randint(1, 10)
nyawa = 3

while True:
    print ("angka :", angka)
    tebak = int(input("Masukan angka :"))
    if tebak == angka:
        print("benar!")
        break
    else :
        print("salah!")
        nyawa -= 1
        print("Nyawa :", nyawa)
    if nyawa == 0:
        print("game over")
        break