#arena_training
import random

def attack():
    return random.randint(10, 20)
def heal():
    return random.randint(5, 15)
def status(hp_player, hp_monster):
    print("===STATUS===")
    print("Player :", hp_player)
    print("Monster :", hp_monster)
    print("============")

hp_player = 100
hp_monster = 100

while hp_player > 0 and hp_monster > 0:
    status(hp_player, hp_monster)
    pilih = input("pilih A/B :")
    if pilih == "A":
        damage = attack()
        print("Damage :", damage)
        hp_monster -= damage
    elif pilih == "B":
        darah = heal()
        print("Heal :", darah)
        hp_player += darah
        if hp_player > 100:
            hp_player = 100
    else :
        print("Ulangi")
    
    if hp_player <= 0:
        print("Game over")
        break
    elif hp_monster <= 0:
        print("Win!")
        break
