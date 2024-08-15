print("Fibonacci Dizisi Oluşturma Programına Hoş Geldiniz!!!")

sayi = int(input("Kaç elemanlı Fibonacci dizisi oluşturmak istediğinizi girin:"))

if sayi <= 0:
    print("Lütfen pozitif bir sayı giriniz.")
else:
    # Fibonacci dizisini oluştur
    liste = [0, 1]
    while len(liste) < sayi:
        liste.append(liste[-1] + liste[-2])

    # İstenilen eleman sayısından fazla olursa kes
    liste = liste[:sayi]


    print(f"İlk {sayi} Fibonacci sayısı: {liste}")