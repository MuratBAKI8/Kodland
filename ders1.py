import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("şifren kaç karakter olsun"))
password = ""
for i in range(uzunluk):
    password += random.choice(karakterler)
print(password)
