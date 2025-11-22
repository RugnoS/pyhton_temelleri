#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonskiyonu yazın

# def yazdir(kelime,adet):
#     print(kelime*adet)

# yazdir("merhaba",10) #eğer merhaba kelimesinin yanına \n yazarsak alt alta yazar


#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon hazırlayın

# def listeyeCevir(*args):
#     liste = []
    
#     for param in args:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,"merhaba")
# print(result)

#gönderilen 2 sayı arasındaki tüm asal sayıları bulun



# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input("sayı1: "))
# sayi2 = int(input("sayı2: "))

# asalSayilariBul(sayi1,sayi2)
#kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün,

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if sayi %i==0:
            tamBolenler.append(i)
    
    return tamBolenler

print(tamBolenleriBul(20))
