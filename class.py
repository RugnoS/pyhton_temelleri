#bilmemiz gereken kavramlar class, object(instance)
#class
class Person:
    #class attributes
    address = "no information"
    #constructor(yapıcı metod)
    def __init__(self, name, year): #self ilk parametrede yer alır her hangi bir şeyde denir
        #object attribustes
        self.name = name
        self.year= year
        print("init metodu çalıştı")
    # methods

#object(instance)
p1 = Person("ali",1990)  # iki farklı adreste obje
p2 = Person("yağmur",1995)
#uptading 
p1.name ="ahmet"
p1.address = "kocaeli"
#accsesing object attribustes
print(f"name: {p1.name} , year : {p1.year} address:{p1.address}")
print(f"name: {p2.name} , year : {p2.year} address:{p2.address}")