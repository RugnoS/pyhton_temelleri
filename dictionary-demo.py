# ogrenciler = {
#     "120" : {
#         "ad" : "Ali",
#         "soyad" : "Yılmaz",     
#         "telefon" : "532 000 00 01"    
#     },
#     "125" : {"ad" : "Can",
#              "soyad" : "Korkmaz",
#              "telefon" : "532 000 00 02"
#              },
#              "128": {
#                  "ad":"Volkan",
#                  "soyad" : "Yükselen",
#                  "telefon" : "532 000 00 03"
#              },
# }

# bilgileri verilen öğrencileri kullanıcadan aldığınız bilgilerle
#dictirnary icinde saklayınız

#öğrenci numarasını kullanıcadan alıp ilgili öğrenci bilgisini gösteriniz

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
soyad = input("Öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : soyad,
#     "telefon" : phone
# }
#uptade de birden çok teklarlayabilirz
ogrenciler.update({
    number:{
        "ad" : name,
        "soyad" : soyad,
        "telefon" : phone

    } 
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
soyad = input("Öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        "ad" : name,
        "soyad" : soyad,
        "telefon" : phone

    } 
})


number = input("öğrenci no: ")
name = input("öğrenci adı: ")
soyad = input("Öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        "ad" : name,
        "soyad" : soyad,
        "telefon" : phone}})

# print(ogrenciler)

print("*"*50)
ogrNo  = input("öğrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)


print(f"Aradgınız {ogrNo} nolu öğrencinin adı :{ogrenci["ad"]} soyadı:{ogrenci["soyad"]} ve telefonu ise {ogrenci["telefon"]} ")