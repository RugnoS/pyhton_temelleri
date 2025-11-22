name = "mustafa"
surname = "songur"
age = "24"

# print("my name is"+ name + " "+ surname + "and \nI am " + age + "years old.")

greeting = "my name is"+ name + " "+ surname + "and \nI am " + age + "years old."
# \ ters slash bir alt satıa devam ettirir
print(greeting)

#string ifadelerde soldan sağa ilk karakterden son karaktere 0 dan başlayarak devam eder.
#ifadedenin kaç karakterli olduğunu öğrenmek istersek len ifadesini kullanırız.
print(greeting[3])

# length = len(greeting)
# print(length)
# print(greeting[length-1])
# print(greeting[-1])
# bir aralık belirtmek istersek örn
# print(greeting[3:7])
#başlangıcı yazıp bitişi boş bırakırsak başlar sona kadar gider veya tam tersi
#print(greeting[9:])
#eğer ki şurda başla şurda bştşr ama her iki karakterden birini al dersek şu şekilde yaparız
# print(greeting[2:44:2])
