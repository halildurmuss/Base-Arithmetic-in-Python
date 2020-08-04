

                    #VAR OLAN TABAN ALINIYOR
def get_source_base():
    a=input("Lütfen çevireceğiniz sayının tabanını giriniz: ")
    if int(a)!=2 and int(a)!=8 and int(a)!=10 :
        while int(a)!=2 and int(a)!=8 and int(a)!=10 :
         print("Geçerli taban girmediniz. Geçerli tabanlar 2, 8 ve 10'dur. Lütfen yeniden deneyin.")
         a=input("Lütfen çevireceğiniz sayının tabanını giriniz: ")

    return a
                    #DÖNÜŞTÜRÜLECEK  TABAN ALINIYOR
def get_target_base():
     a=int(input("Lütfen sayının dönüştürüleceği hedef tabanı giriniz: "))
     if a != 2 and a != 8 and a != 10:
         while a != 2 and a != 8 and a != 10:
             print("Geçerli taban girmediniz. Geçerli tabanlar 2, 8 ve 10'dur. Lütfen yeniden deneyin.")
             a = int(input("Lütfen sayının dönüştürüleceği hedef tabanı giriniz: "))
     return a

                    #ÇEVRİLECEK SAYIYI ALMA
def get_number(taban):

            a=input("Lütfen çevrilecek sayıyı giriniz: ")
            while a:
                for i in a:
                    if int(i)>=taban:
                        print(taban,"tabanında geçerli bir sayı girmediniz (",i,">=",taban,") Lütfen yeniden deneyin.")
                        a = input("Lütfen çevrilecek sayıyı giriniz: ")
                        break
                if int(i)<taban:
                    break
            return a

                    #10 TABANINDAN 2 VEYA 8 E ÇEVİRME
def convert_10_to_base(number,base):
    #newInt =input("Sayi giriniz.")
    yeniSayi=int(number)
    karakter=""
    while yeniSayi > 0:
        karakter= str(yeniSayi% base) + karakter
        yeniSayi = yeniSayi // base

    print("10 luk tabandan 2 veya 8 e : ",karakter)

                    #2 VEYA 8 TABANINDAN 10 TABANINA ÇEVİRME
def convert_base_to_10(sayi, sayi_tabani):
        yeniSayi = int(sayi)
        karakter = 0
        print("sdfg")
        a = 0
        while yeniSayi > 0:
            karakter = (yeniSayi % 10) * sayi_tabani ** a + karakter
            a = a + 1
            yeniSayi = yeniSayi // 10
        print("2 veya 8 den 10 luk tabana: ", karakter)
                    #DÖNÜŞTÜRME İŞLEMİ
def convert_number(source_base,target_base, number):
       if target_base == 10 :
           def convert_base_to_10(sayi, sayi_tabani):
               yeniSayi = int(sayi)
               karakter = 0
               a = 0
               while yeniSayi > 0:
                   karakter = (yeniSayi % 10) * sayi_tabani ** a + karakter
                   a = a + 1
                   yeniSayi = yeniSayi // 10
               print(karakter)
           return convert_base_to_10(number,source_base)

       elif source_base==10 :#10
           def convert_10_to_base(sayi, sayi_taban):
               # newInt =input("Sayi giriniz.")
               yeniSayi = int(sayi)
               karakter = ""
               while yeniSayi > 0:
                   karakter = str(yeniSayi % sayi_taban) + karakter
                   yeniSayi = yeniSayi // sayi_taban

               print(karakter)
           return convert_10_to_base(number,target_base)

       elif target_base==8 and source_base==2:

           def convert_base_to_10(sayi, sayi_tabani):
               yeniSayi = int(sayi)
               karakter1 = 0
               a = 0
               while yeniSayi > 0:
                   karakter1 = (yeniSayi % 10) * sayi_tabani ** a + karakter1
                   a = a + 1
                   yeniSayi = yeniSayi // 10

               b = int(karakter1)
               a = ""
               sayi_tabani=8
               while b > 0:
                   a = str(b % sayi_tabani) + a
                   b = b // sayi_tabani
               print(a)
           return convert_base_to_10(number, source_base,)

       elif target_base==2 and source_base==8:

           def convert_10_to_base(sayi, sayi_tabani):
               yeniSayi = int(sayi)
               karakter1 = 0
               a = 0
               while yeniSayi > 0:
                   karakter1 = (yeniSayi % 10) * sayi_tabani ** a + karakter1
                   a = a + 1
                   yeniSayi = yeniSayi // 10

               b = int(karakter1)
               a = ""
               taban=2
               while b > 0:
                   a = str(b % taban) + a
                   b = b // taban
               print(a)
           return convert_10_to_base(number, source_base,)

k=int(get_source_base()) #ÇEVRİLECEK OLAN SAYININ TABANI
h=int(get_target_base()) #DÖNÜŞECEĞİ SAYI TABANI
t=get_number(k)         #SAYİ ALINIYOR
convert_number(k,h,t)
