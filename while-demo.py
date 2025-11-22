sayilar = [1,3,5,7,9,12,19,21]

#sayılar listesini while ile ekrana yazdırın 

# i=0
# while i< len(sayilar):
#     print(sayilar[i])
#     i+=1 

#başlangıc ve bitiş değelerini kullanıcıdan alıp aradaki tek sayıları ekrana yazıdırın
# a = int(input("1.sayı"))
# b = int(input("2.sayı"))
# i = a
# while i < b:
#     i += 1
#     if i %2==1:
#         print(i)
       

 # 3 ile 100 arasında ki sayıları azalan şekilde yazın
# i = 100
# while i > 3:
#     i -=1
#     print(i)    


#kullanıcıdan 5 sayı alın sıralı bir şekilde ekrana yazıdırın

# numbers = []
# i = 0
# while i<5:
#     sayi = int(input("sayı: "))
#     numbers.append(sayi)
#     i += 1
#     numbers.sort()
#     print(numbers)

#kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesinde saklayın
#urun sayısını kullanıcıya osurn
#dictionary liste yapısı (name,price) şeklinde olsun
#ürün ekleme işlemi bittiğinde ürünleri ekrana wihlw ile yazdırın

# urunler = []

# adet = int(input("kaç adet ürün eklemek istiyorsunuz :"))
# i=0

# while i<adet:
#     name = input("ürün ismi :")
#     price = input("ürün fiyatı: ")
#     urunler.append({
#         "name":name,
#         "price":price
#     })
#     i +=1

# for urun in urunler:
#     print(f"ürün adı {urun["name"]} ve ürün fiyatı {urun["price"]}")