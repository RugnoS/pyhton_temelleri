hesapA = {
    "ad": "sadık turan",
    "hesapNo":"13245678",
    "bakiye":3000,
    "ekhesap":2000
}

hesapB = {
    "ad": "ali turan",
    "hesapNo":"12345678",
    "bakiye":2000,
    "ekhesap":1000
}

def paraCek(hesap, miktar):
    print(f"merhaba {hesap["ad"]}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -=miktar
        print("paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"] + hesap ["ekhesap"]

        if(toplam >=miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanimi == "e":
                 ekHesapKullanilicakMiktar = miktar - hesap["bakiye"]
                 hesap["bakiye"] = 0
                 hesap["ekhesap"] -= ekHesapKullanilicakMiktar
                 print("paranızı alabilirsiniz")
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır.")
        else:
            print("üzgünüz bakiye yetersiz")
            

def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} tl bulunmaktadır . eh hesabınızda  {hesap["ekhesap"]} tl bulunmaktadır ")
paraCek(hesapA,4000)
bakiyeSorgula(hesapA)  #bakiye sorgulayı her para çekme işleminden sonrada verebiliriz işlemi sürekli tekrarlayabilirz