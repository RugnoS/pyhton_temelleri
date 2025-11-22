#ödev sayfam değişen ödevi
#1- bir müşterinin aşşağıdaki bilgileri için değişken oluşturunuz
# müşteri adı,soyadı,,ad soyad,cinsiyet,tc kimlik,doğumyılı,adres bilgisi,yaşı
musteriAdi = "mustafa"
musteriSoyadi = "songur"
musteriAdSoyad =  musteriAdi + " " + musteriSoyadi 
musteriCinsiyet = True # Erkek
musteriDogumyili = 2001
musteriAdres = "sivas hafik"
musteriYasi = 2025 - musteriDogumyili
müsteritckimlik = "024838233429"
print(musteriAdSoyad)
print(musteriYasi)

#aşşağıdaki siparişlerin toplam bilgsini hesaplayınız.

siparis1 = 110
siparis2 = 192
siparis3 = 321.21
total = siparis1 + siparis2 + siparis3
print(total) 

print(siparis1 + siparis2 + siparis3)

'''
Daire Alanı : πr**2
Daire Çevresi : 2πr

YARI ÇAPI VERİLEN BİR DAİRENİN ALAN VE ÇEVRESİNİ HESAPLAYINIZ r=3.14

'''
pi = 3.14

yaricap = float(input("yarı çapı : "))

alan = pi *( yaricap **2)
cevre = 2 * pi * yaricap

print("alan", alan )
print("çevre" , cevre )
print("alan: " +str(alan) +" çevre :"+str(cevre))

      