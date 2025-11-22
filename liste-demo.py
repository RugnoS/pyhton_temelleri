#Bmw, Mercedes,opel,Mazda elamanlarıyla bir liiste oluşturunuz

# result = ["bmw","mercedes","opel","mazda"]
# print(result)


#liste kaç elemanlıdır

# print(len(result))


#listenin ilk ve son elemanı nedir?

# ilk = result[0]
# son = result[3]
# print(ilk)
# print(son)


#mazda değerini toyota ile değiştirin

# result[-1] = "Toyata"
# print(result)


#mercedes listenin bir elemanımıdır?
# keyif = "mercedes" in  result
# print(keyif)


#listenin -2 indeksindeki değer nedir
# arabalar =  result[-2]
# print(arabalar)


#listenin ilk üç elemanını alın
# arabalar = result[0:3]
# print(arabalar)


# son iki eleman yerine toyata ve reno yu ekleyin
# result[-2:] = "toyata", "reno"
# print(result)


# #listenin üzerine audi ve nissan ekleyin
# result1 = ["audi","mercedes"]
# arabalar = result1 + result
# # # print(arabalar)


# # #listenin son elemanını silin 
# # del arabalar[-1]



# #elemanları tersten yazıdralım
# caney = arabalar[::-1]
# print(caney)


#aşşağıdaki verileri liste içinde saklayınız 

#studentA: Yiğit Bilgi 2010, (70,60,70)
#studentB: Sena Turan 1999, (80,80,70)
#studentC: Ahmet Turan 1998, (80,70,90)

# studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
# studentB = ["Sena","Turan",1999,[80,80,70]]
# studentC = ["Ahmet","Turan",1998,[80,70,90]]
# result = studentA[0]
# result = studentB[2]
# result = studentC[3][2]

# result = f"{studentA[0]} {studentA[1]} {2025-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"












# print(result)