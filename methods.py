# #class
# class Person:
#     #class attributes
#     address = "no information"
    
#     #constructor(yapıcı metod)
#     def __init__(self, name, year): #self ilk parametrede yer alır her hangi bir şeyde denir
        
#         #object attribustes
#         self.name = name
#         self.year= year
    
#     #instance methods
#     def intro(self):
#         print("hello there ı am "+ self.name)
#     #instance methods
#     def calculateAge(self):
#         return 2025 - self.year
# #object(instance)
# p1 = Person("ali",1990)  # iki farklı adreste obje
# p2 = Person("yağmur",1995)
# p1.intro()
# p2.intro()

# print(f"adım : {p1.name} ve yaşım: {p1.calculateAge()}")
# print(f"adım : {p2.name} ve yaşım: {p2.calculateAge()}")

class Circle:
    #class objecy attribute
    pi=3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1= Circle() #belirtmezsek bir olarak algılar öyle belirttiğimiz için
c2 = Circle(5)
print(f"c1 alan = {c1.alan_hesapla()} çevre {c1.cevre_hesapla()}")
print(f"c2 alan = {c2.alan_hesapla()} çevre {c2.cevre_hesapla()}")