numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]


val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40 #değiştirmek için kullanılır
numbers.append(49)  #en sona ekler
numbers.insert(3, 78) #index bilgisi verilir

# numbers.pop()
numbers.pop(2) #sıralamadan siler
numbers.remove(49) #verdiğib sayıyı siler
numbers.sort() #listeyi sıralar
numbers.reverse() #sıralanan listeyi ters çevirir
print(len(numbers))



print(numbers.count(10)) #içerisinde kac adet olduguunu söyler


print(numbers)
