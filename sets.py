fruits = { "orange", "apple", "banana"}

# print(fruits)[0]
#indexlenemez liste türüdür

#elemanlara şu şelilde ulaşılır

for x in fruits:
    print(x)


fruits.add("cherry") #şeklinde eleman eklenir

#alternatif olarak
fruits.update(["mango"])
print(fruits)

fruits.remove("mango") #kaldırmak icin kullanılır
#.discard da silmenin bir altarnatifidir
#bu listelerde bir elemandan sadece bir kez olur

# myList = [1,2,3,4,1,2,3,2,1]

# print(set(myList))