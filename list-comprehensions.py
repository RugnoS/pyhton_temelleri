for x in range(10):  #normalde
    print(x)

numbers = [x for x in range(10)] # liste şeklinde yapmak icin #yeni yöntem
print(numbers)

for x in range(10): #normal
    print(x**2)

numbers = [x**2 for x in range(10)] # liste şekli
print(numbers)

numbers = [x**2 for x in range(10) if x%3 ==0] #sadece üce bölünenler gözüksün örneğin
print(numbers)

myString = "hello"
myList = []

for letter in myString: #eski yöntem
    myList.append(letter)
print(myList)

myList = [letter for letter in myString] 
print(myList) # yeni yöntem

years = [1983,1999,2008,1956,1986]
ages = [ 2025 - year for year in years]
print(ages)



results = [x if x%2==0 else "tek" for x in range(1,10)]
print(results)