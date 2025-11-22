x = 5
hak = 5
devam = "e"
result = 5 <= x < 10


#and ikiside doğru olması gerekiyor
result = (x > 5 and x < 10)
result = hak > 0 and devam == "e"



#or sadece biri doğru olsa yeter true,true=true true,false=true false,false=false

result = x>0 or (x%2==0)


#not tersini veerir

result = not(x>0)

#x , 5-10 arasında bir çift sayı mı ?
result = (x>5 and x<10) and (x%2==0)
print(result)