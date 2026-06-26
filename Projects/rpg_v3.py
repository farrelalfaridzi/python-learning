# RPG V3
# Dibuat oleh Farrel
#
# Materi:
# - Function
# - Random
# - While Loop
# - If Else
# - Variabel
# - Operator Matematika

import random

hp_player = 100
hp_monster = 100
gold = 100
sword = False

def attack():
    return random.randint(20, 30)
def heal():
    return random.randint(10, 20)
def status(hp_player, hp_monster, gold, sword):
    print("===STATUS===")
    print("player :", hp_player)
    print("monster :", hp_monster)
    print("GOLD :", gold)
    print("SWORD :", sword)
    print("============")

while hp_player > 0 and hp_monster > 0:
    print("===ACTION===")
    print("1. attack")
    print("2. heal")
    print("3. shop")
    print("4. status")
    print("5. exit")
    print("============")
    
    #player
    pilih = input("pilih aksi :")
    if pilih == "1":
        damage = attack()
        if sword == True:
            damage *= 2
        hp_monster -= damage
        gold += 15
        print ("DAMAGE :", damage)
        print ("Gold :", gold)
        if hp_monster <= 0 :
            print("WIN!")
            break
    elif pilih == "2":
        darah = heal()
        hp_player += darah
        print ("DARAH BERTAMBAH :", darah)
    elif pilih == "3":
        print("===SHOP===")
        print("1. potion : 10")
        print("2. sword : 30")
        print("==========")
        print("GOLD :", gold)
        if gold <= 0 :
            print ("tidak cukup")
        shop = input("pilih aksi :")
        if shop == "1" and gold >= 10:
            gold -= 10
            hp_player += 10
            print ("potion dibeli, drah bertamabh : 10")
        elif shop == "2" and gold >= 30:
            if sword == True:
                print("sword sudah dibeli")
            else :
                gold -= 30
                print("sword berhasil dibeli")
                sword = True
        else :
            print("gold tidak cukup")
        print("GOLD :", gold)
    elif pilih == "4":
        status(hp_player, hp_monster, gold, sword)
    elif pilih == "5":
        print ("terima kasih!")
        break
    else :
        print("tidak valid")

    #monster
    damage_monster = random.randint(5, 15)
    hp_player -= damage_monster
    print("monster menyerang!")
    print("damage :", damage_monster)

    #condition
    if hp_player <= 0 :
        print("GAME OVER!")
        break