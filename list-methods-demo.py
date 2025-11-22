names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998,2000,1998,1987]
#cenk ismini listenin sonunna ekleyiniz
names.append("cenk")
#sena ismini başa ekleyiniz
names.insert(0,"sena")
#deniz ismini listeden siliniz
names.remove("Deniz")
#hakan isminin indexi nedir
index = names.index("Hakan")
#ali listenin bi elamanımıdır ) 
result = "Ali" in names
#liste elemanlarını ters çevirin
names.reverse()
#liste elemanlarını sıralayın alfabetik
names.sort()
#years listesini büyüklüğe göre sıralayınız
years.sort()
#str = "chevrolet,dacia" dizisini listeye çveriniz
str = ["chevrolet", "dacia"]
#years dizisinin en büyük ve en küçük elamanı nedir
min = min(years)
max = max(years)
#years dizisinde kac tane 1998 değeri vardır
print(years.count(1998))
#years dizisinde tüm elemanları siliniz.
years.clear
#kullanınıcıdan alacağınız 3 marka bilisigini saklayınız
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)






















