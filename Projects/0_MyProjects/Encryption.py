def kodla(metin):
    kodlandı = []
    for harf in metin:
        if harf.isalpha():
            if harf == 'z':
                kodlandı.append('a')
            elif harf == 'Z':
                kodlandı.append('A')
            else:
                kodlandı.append(chr(ord(harf) + 1))
        else:
            kodlandı.append(harf)
    return ''.join(kodlandı)

def kodu_coz(metin):
    cozuldu = []
    for harf in metin:
        if harf.isalpha():
            if harf == 'a':
                cozuldu.append('z')
            elif harf == 'A':
                cozuldu.append('Z')
            else:
                cozuldu.append(chr(ord(harf) - 1))
        else:
            cozuldu.append(harf)
    return ''.join(cozuldu)

print("""
**************************
Yapılacak işlemi seçiniz:
1- Kodla
2- Kodu Çöz
3- Çıkış
**************************
""")
while True:
    secim = int(input("İşlemi Seçiniz: "))
    if secim == 1:
        cumle = input("Şifrelenecek cümleyi giriniz: ")
        print("Şifrelenmiş Cümle: ", kodla(cumle))
    elif secim == 2:
        cumle = input("Çözülecek cümleyi giriniz: ")
        print("Çözülmüş Cümle: ", kodu_coz(cumle))
    elif secim == 3:
        break
    else:
        print("Geçersiz seçim...")