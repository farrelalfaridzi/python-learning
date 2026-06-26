# Challenge 12B - Profil Karakter
# Dibuat oleh Farrel
#
# Materi:
# - Dictionary
# - Input Output
# - Variabel

player = {
    "nama" : "",
    "job" : "",
    "level" : 1,
    "hp" : 100
}

nama = input("masukan nama :")
player["nama"] = nama
job = input("masukan pekerjaan :")
player["job"] = job

player["gold"] = 50

print("===KARAKTER===")
print("Nama :", player["nama"])
print("Job :", player["job"])
print("Level :", player["level"])
print("HP :", player["hp"])
print("Gold :", player["gold"])
print("==============")