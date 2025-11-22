# ıdentity operator: is

# x = y =[1, 2, 3]
# z = [1, 2, 3]

# print(x==z)
# print(x is y) # aynı referansta oldugu icin true aynı adres
# print(x is z) #farklı referansta oldugu icin false farklı adres

x = [1, 2, 3]
y = [2, 4]
del x[2]
y[1] = 1
y.reverse()
print(x==y) #true
print(x is y) #false



#membership operator:in

x = ["apple" , "banana"]
print("banana" in x) #içerisinde var mı ? sorususudur