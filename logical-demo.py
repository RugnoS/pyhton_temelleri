#girilen bir sayının 0-100 arasında olup olmadıgını kontrol ediniz
# sayi = int(input("sayı gir: "))
# result = 0<sayi<100


#girilen bir sayının pozitif çift sayı olup olmadıgını kontrol et
# sayi = int(input("sayı"))
# result = (sayi>0) and (sayi%2==0)
# print(result)


#e mail ve parola bilgisleri ile giriş kontrolü yapınız
# mail ="mustson@gmail.com"
# pas ="123456"
# girilenEmail= input("email: ")
# girilenPass= input("pass:")
# result = (girilenEmail == mail) and (girilenPass == pas)

# print(f"girilen mail ve şifre{result}")

#girlen 3 sayıyı büyüklük olarak karşılaştırınız
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# result = (x > y) and (x > z)
# print(f"x en büyük sayıdır : {result}") 

# result = (y > x) and (y > z)
# print(f"y en büyük sayıdır : {result}") 

# result = (z > y) and (z > x)
# print(f"z en büyük sayıdır : {result}") 

#kullanıcadan 2 vize %60 ve final %40 noturunu ortalmasını alıp hesaplayınız
#eğer 50 ve üzeriyse geçti degilse kaldı yazdırın
# ortlama 50 olsa bile final notu en az 50 olmaılır
# b finalden 70 aldıgında ortalamanın önemi olmasın

# vize1 = float(input("vize 1 : "))
# vize2 = float(input("vize 2 : "))
# final = float(input("final : "))
# ortalama = (vize1 + vize2) * 0.3 + (final) * 0.40
# # result = ortalama>=50 and final >= 50
# result = ortalama>=50 or  final >=70
# print(f"öğrencinin ortalaması {ortalama}, ve geçme durumu : {result}")


# kişinin ad kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız
#fformül : kilo/boy uzunlugunun karesi
#aşşağıdaki tabloya göre kişi hangi gruba girer
#0-18.4 zayıf  18.5-24.9 normal  25.0-29.9 fazla kilolu 30.0-34.9 obez

name = input("adınız : ")
kg = float(input("kilonuz : "))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
zayif = index >=0 and index<=18.4
normal = index > 18.4 and index <= 24.9
kilolu = index > 24.9 and index <= 29.9
obez = index >= 29.9 and  index <=34.9


print(f"{name} kilo endeksin : {index} ve kilo değerlendirmen zayıf : {zayif}")
print(f"{name} kilo endeksin : {index} ve kilo değerlendirmen normal : {normal}")
print(f"{name} kilo endeksin : {index} ve kilo değerlendirmen kilolu : {kilolu}")
print(f"{name} kilo endeksin : {index} ve kilo değerlendirmen obez : {obez}")