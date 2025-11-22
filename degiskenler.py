maasAli = 5000
maasAhmet = 4000
vergi = 0.27 

print(5000 - (5000 * 0.27))
print(4000 - (5000 * 0.27))
print(maasAli - (maasAli * vergi))

# Değişken tanımlama Kuralları

# rakam ile başlayamaz

number1 = 10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)

#Büyük Küçük HARF DUYARLILIĞI VARDIR

age = 30 
Age = 24
print(Age)

#Türkçe karakter kullanmayalım

x = 1           # int
y = 2.3              # float
name = "Çınar"         # string    
isStudent = True        # bool

a = 10 
b = 20 
print(a+b) #30 #eğer 10 ve 20 de tırnak verirsen bunu string olarak algılar ve 1020 şeklinde yazar
firstname = "mustafa"
lastname = "songur"
print(firstname  + lastname)