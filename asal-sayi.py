"""soru:
girilen bir sayının asal olup olmadıgını bulun
**asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir"""
sayi = int(input("sayı giriniz: "))
asalmi = True
if sayi ==1:
    print("1 sayısı asal değildir")

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print("sayı asaldır.")
else:
    print("sayı asal değildir.")
