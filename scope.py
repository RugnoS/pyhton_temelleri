#global scope
x = "global x"

def function():
    #local scope
    x ="local x"

function()
print(x)

#eğer ki local scopu kullanırsanız locala göre ama global de en üstte kullanırsanız global gelir eğer ki localda yoksa iki kere global gelir


name = "çınar"

def changeName(new_name):
    name = new_name
    print(name)

changeName("ada")
print(name)


name = "global string"

def greeting():
    name = "çınar"

    def hello():
        print("hello"+name)

    hello()

greeting()  #işlem icinde printin üstünde ki name çınar oldugu icin global ona göre o dur o yüzden hello çınar ifadesi gelir



x = 50
def test():
    global x  #fonksiyon üzerinde global x i kulllanmak istersek global x değişkeni kullanılır
    print(f"x {x}")

    x=100
    print(f"changed x to {x}")

test()
print(x)