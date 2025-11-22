
# **************range*******************
# for item in range(2,100,10):  #2 den başlar 100 a kadar yazar ve 10ar 10 ar artar
#     print(item)

# print(list(range(2,100,10))) # listeye döndürür


#**************enumerate*****************


# gretting = "hello there"
# for  index,letter in enumerate(gretting):
#     print(f"index: {index} letter : {letter}")  #enumerate indexe karşılık geleni direkt verir 

   
#**********zip***********

list1 = [1,2,3,4,5]
list2= ["a","b","c","d","e"]

print(list(zip(list1,list2))) #listeli 1,a şekline döndürür birleştirir

for item in zip(list1,list2):  # for şeklinde alt alta sıralamak icin
    print(item)