# def changeName(n):
#     n = "ada"

# name = "yiğit"
# changeName(name)
# print(name)


# def change(n):
#     n[0]  = "istanbul"

# sehirler = ["ankara","izmir"]  # listedeki ilk elemanı değiştirir orjinal referanstaki adres aynı kalır

# change(sehirler[:]) #yeni bir kopyasını yazdırırız orjinal kopyasını
# change(sehirler)

# print(sehirler)

# def add(a,b,c=0): #eğer ücüncü yoksa 0 a eşitleyerek veriyi vermezsek 0 a eşitlenir
#     return sum((a,b)) #sum toplamak icindir

# print(add(10, 20))

# #yada

# def add(*params):  # bu şekilde sınırsız veri girebiliriz
#     return sum((params))

# print(add(10,20,30,40,50))


def displayUser(**args):  #dictinory formatı icin
    for key,value in args.items():
        print("{} is {}".format(key,value))
displayUser(name="çınar" , age = 2 ,city="istanbul")
displayUser(name="ada" , age = 12 ,city="kocaeli",phone="1234123")
displayUser(name="çağrı" , age =14 ,city="konya",phone="14324142",email = "naber@gmail.com")


#** çift yıldız dic bilgisini verirken * yıldız sınırsız veri girmemizi sağlar