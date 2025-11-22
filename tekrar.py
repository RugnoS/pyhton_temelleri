bakiye = 5000
def para_cek(bakiye, cekilecek_miktar):
    kalan_para= int((( bakiye - cekilecek_miktar )))
    if cekilecek_miktar > bakiye:
        print("yetersiz bakiye")
        return bakiye
    else:
        bakiye=kalan_para
        print(f"yeni bakiye: {kalan_para}")
    return kalan_para
    
    
while True:
    cekilecek_miktar=int(input("çekilecek tutarı giriniz: "))
    if cekilecek_miktar==0:
        print("çıkış yapılıyor..")
        break
    bakiye = para_cek(bakiye, cekilecek_miktar)
    