import random

def lempar_dadu():
    return random.randint(1, 6)

total = 0
lemparan = 0

while lemparan < 5:
    dadu = lempar_dadu()
    lemparan += 1
    print ("lemparan", lemparan, ":", dadu)
    total += dadu

print("Total :", total)