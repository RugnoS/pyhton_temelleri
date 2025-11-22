# def sayHello(name = "user"): #eğer name belirtilmezse user belirtilir
#     print("Hello" + name)


# yada

def sayHello(name = "user"): #eğer name belirtilmezse user belirtilir
   return "Hello" + name

msg = sayHello("ada") # her kullandığımızda gelir
print(msg)

def total(num1, num2):
   return num1 + num2

result =  total(10,20)
print(result)

def yasHesapla(dogumYili):
   return 2025 - dogumYili

ageCinar = yasHesapla(2017)
ageGuray = yasHesapla(2000)
ageMustafa = yasHesapla(2001)

print(ageCinar, ageGuray, ageMustafa)

def EmekliligeKacYilKaldi(dogumYili, isim):
   yas = yasHesapla(dogumYili)
   emeklilik = 65 - yas
   if emeklilik > 0:
      print(f"emekliliğine {emeklilik} yıl kaldı")
   else:
      print("zaten emekli oldunuz")


EmekliligeKacYilKaldi(1998, "Ali")