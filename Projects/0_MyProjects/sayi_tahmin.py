import random
import time

print("""**********************************************

Sayı Tahmin Oyunu, Çıkmak için 'q' giriniz...

**********************************************""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7

while True:

    tahmin = (input("Sayi Tahmininizi Giriniz:"))

    if (tahmin == "q"):
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        break

    tahmin = int(tahmin)

    if (tahmin < rastgele_sayi):
        print("Hesaplanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz.")
        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayi):
        print("Hesaplanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz:")
        tahmin_hakki -= 1

    else:
        print("Hesaplanıyor...")
        time.sleep(1)
        print("Doğru tahmin!!!")

    if (tahmin_hakki == 0):
        print("Tahmin hakkınız kalmadı. Sayı:",rastgele_sayi)
        break
