'''
x = input("1.sayı: ")
y = input("2.sayı: ")

print(type(x))
print(type(y))      

toplam = int(x) + int(y)
print(toplam)
#inputtan gelen değerler string olarak gelir bunun icin başlarına int getirlir
'''
x = 5 #int
y = 2.5 #float
isim = "çınar" #string
isOnline = True #bool
# Type Conversion

# int to float

x = float(x)
print(x)
print(type(x)) 

#float to int
y = int(y)
print(y)
print(type(y))

result = x + y 
print(result)
print(type(result))

result = int(result)
print(result)
print(type(result))

# # bool to str
# isOnline = str(isOnline)
# print(isOnline)

#bool to int
isOnline = int(isOnline)
print(isOnline)

      


