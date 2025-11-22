x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

 #kullanıcıdan aldıgınız 2 sayının çarpımı ile xyz nin toplamının farkı nedir ?

# a = int(input("1.sayı: "))
# b = int(input("2.sayı: ")) 

# result = (a * b) - (x+y+z)
# print(result)


#y nin x e kalannsız bölümünü hesaplayınız

# result =  y // x 
# print(result)


#(x,y,z) toplamının mod 3 ü nedir

# result = (x+y+z) % 3
# print(result)

# y nin x inci kuvvetiniz hesaplayınız

# result = y**x
# print(result)


# x, *y, z = numbers işşlemine göre z nin küpü kaçtır

# x, *y, z = numbers

# result = z**3
# print(result)


#x, *y, z = numbers işşlemine göre y nin değerleri toplamı kaçtır
x, *y, z = numbers
result = y[0] + y[1] + y[2]
print(result)


