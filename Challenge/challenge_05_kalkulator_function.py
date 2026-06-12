#kalkulator
def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    return a / b

a = int(input("Angka pertama :"))
operasi = input("Operasi +/-/*/(/) :")
b = int(input("Angka kedua :"))
if operasi == "+":
    hasil = tambah(a, b)
elif operasi == "-":
    hasil = kurang(a, b)
elif operasi == "*":
    hasil = kali(a, b)
elif operasi == "/":
    hasil = bagi(a, b)

print(hasil)