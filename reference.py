#value typs string float int

x = 5 
y = 25

x = y

y = 10

# print(x,y)

#y nin üzerinde sonradan yaptığınız değişiklik xi etkilemez.

#references type

a = ["apple" , "banana"]
b = ["apple", "banana"]
a = b 
b[0] = "grape"
print(a,b) 
#reference typda b nin üzerinde yaptığınız değişiklik a yıda etkiler