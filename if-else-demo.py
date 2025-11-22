#kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet
# alıp alamama durumunu kontrol ed,n 18y aş üstü ve eğitim lise veya üni olmalıdır

# ad = input("isim : ")
# yas = int(input("yaşınız : "))
# egitim = input("eğitim bilginiz")
# if yas >=18 : 
#     if (egitim == "üniversite" or egitim =="lise"): 
#         print("ehliyet alabilirsiniz")
#     else :
#         print("ehliyet alamazsınız")
# else:
#     print("ehliyet alamazsınz")

# bir öprencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not bilgisini yazdırınız
# yazili1 = float(input("1.yazıllı: "))
# sozlu = float(input("sözlü: "))
# yazili2 = float(input("2.yazıllı: "))
# ort = (yazili1+yazili2+sozlu)/3
# if ort>=0 and ort<25:
#     print(f"ortlamanız: {ort} notunuz:0")
# elif ort >= 25 and ort<45:
#     print(f"ortlamanız: {ort} notunuz:1")
# elif ort >= 45 and ort<55:
#     print(f"ortlamanız: {ort} notunuz:2")
# elif ort >= 55 and ort<70:
#     print(f"ortlamanız: {ort} notunuz:3")
# elif ort >= 70 and ort<85:
#     print(f"ortlamanız: {ort} notunuz:4")
# elif ort >= 85 and ort<101:
#     print(f"ortlamanız: {ort} notunuz:5")
# else:
#     print("yanlış bilgi girdiniz.")

#trafiğe çıkış tarihi alınan bir aracın servis zamanını aşşağıdaki bilgilerle hesaplayyıınız
#1.bakım = 1.yıl
#2.bakım= 2.yıl
#3.bakım=3.yıl
#** süre hesabında alınan gün ay yıla göre gün bazlı hesaplayınız
#datetime modlunu kullanın
# simdi-2018/8/1>gün
import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis

days=fark.days
print(days)
if days<=365:
    print("1.servis aralığı")
elif days> 365 and days<=365*2:
    print("2.servis aralaığı")
elif days>365*2 and days<=365*3:
    print("3.servis aralığı")
else:
    print("hatalı süre bilgisi")

 