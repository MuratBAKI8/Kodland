oyunkarakterleri_sozlugu = {
  "FREEMAN": "Half Life serisinin ana karakteridir",
  "CHELL": "Portal serisinin ana karakteridir",
  "GMAN": "Half life ta Gordon ı Yönertirken bizi izleyen kimliği belirsiz kişi"
}
karakter = input("hangi karakteri aramak istiyorsun(hepsini büyük yaz)")

if karakter in oyunkarakterleri_sozlugu.keys():
    print(oyunkarakterleri_sozlugu[karakter])

else:
    print("böyle bir karakter sözlükte yok")
