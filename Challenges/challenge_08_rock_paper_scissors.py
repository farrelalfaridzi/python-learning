#batu gunting kertas
#dibuat oleh farrel

import random

pilihan = ["BATU", "GUNTING", "KERTAS"]
game = "Y"

while game == "Y":
    print ("===BATU,GUNTING,KERTAS===")
    print ("A. BATU")
    print ("B. GUNTING")
    print ("C. KERTAS")
    print ("=========================")

    player = input("pilih :")
    player = player.upper().strip()
    if player == "A":
        player = "BATU"
    elif player == "C":
        player = "KERTAS"
    elif player == "B":
        player = "GUNTING"
    komputer = random.choice(pilihan)
    print ("player :", player)
    print ("komputer :", komputer)

    if player == komputer :
        print("SERI")
    elif player == "BATU" and komputer == "GUNTING" :
        print ("MENANG")
    elif player == "BATU" and komputer == "KERTAS":
        print ("KALAH")
    elif player == "GUNTING" and komputer == "BATU":
        print("KALAH")
    elif player == "GUNTING" and komputer == "KERTAS":
        print("MENANG")
    elif player == "KERTAS" and komputer == "BATU":
        print("MENANG")
    elif player == "KERTAS" and komputer == "GUNTING":
        print("KALAH")
    else :
        print("tidak valid")

    restart = input("mau main lagi? Y/N:").upper().strip()
    if restart == "Y":
        game = "Y"
    elif restart == "N":
        break