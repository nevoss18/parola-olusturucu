import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Parolanın uzunlugunu giriniz: "))

parola = ""

for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

print("Parola: " + parola)
