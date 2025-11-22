# # key : value

# # 41 = kocaeli 34 = istanbul

# sehirler = ["kocaeli","istanbul"]
# plakalar = [41, 34]
# print(plakalar[sehirler.index("kocaeli")])

# #print(plakalar["kocaeli"]) :> 41 e götürmesi lazım

# # plakalar = { "key" : "value"}
# plakalar = { "kocaeli" : 41 , "istanbul" : 34}

# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# print(plakalar)

users = {
    "sadikturan" : {"age" :36,
"email" : "sadik@gmail.com",
"telefon" : 842391439,
"adress" : "bursa"                },
    "cinarturan" : {"age" :2,
 "roles": ["admin","user"],                   
"email" : "cinar@gmail.com",
"telefon" : 84232439,
"adress" : "istanbul"}
}
print(users["sadikturan"])
print(users["cinarturan"])
print(users["cinarturan"]["roles"][0])
