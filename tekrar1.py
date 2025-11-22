#hesap fabrikası kalıp
class Hesap:
#hesap açarken isim ve para gerekli zorunluluk
    def __init__(self, isim, bakiye):
        self.isim= isim
        self.bakiye=bakiye
        print(f"hoşgeldin {self.isim} , Hesabın oluşturuldu.")
# bu hesap para çekeibilir methodu
    def para_cek(self,miktar):
        if miktar> self.bakiye:
            print("yetersiz bakiye!")
        else:
            self.bakiye= self.bakiye - miktar
            print(f"işlem başarılı. yeni bakiye:{self.bakiye}")
#fabrikayı test edelim
#ilk hesabı üretelim
musteri1=Hesap("mustafa",5000)
musteri2=Hesap("sevcan",3000)
#mustafa islem yapıyor
musteri1.para_cek(2000)
#sevcan işlem yapıyor
musteri2.para_cek(4000)

