#print("Kérem a születési dátumodat: ")
# datum = input()
# datum = datum.replace(".","0")
#
# osszeg = 0
#
# for x in datum:
#     osszeg+=int(x)
#
# #print("1. összeg:",osszeg)
#
# if osszeg>=500:
#     vegleges=osszeg+""
#     vegleges=str(osszeg)
#     osszeg=0
#
#     for x in vegleges:
#         osszeg+=int(x)

# print("Az életszamjegyed:",osszeg)

print("Kérek egy IBAN számot:")
iban = input()

if len(iban)>=15 and len(iban)<=31:
    #ide jön, ha jó
    uj=""

    for x in iban:
        if x.isnumeric():
            uj+=x
        else:
            x=x.lower()
            if x=="a":
                uj+=str(10)
            elif x=="b":
                uj+=str(11)
            elif x=="c":
                uj+=str(12)
            elif x=="d":
                uj+=str(13)
            elif x=="e":
                uj+=str(14)
            elif x=="f":
                uj+=str(15)
            elif x=="g":
                uj+=str(16)
            elif x=="h":
                uj+=str(17)
            elif x=="i":
                uj+=str(18)
            elif x=="j":
                uj+=str(19)
            elif x=="k":
                uj+=str(20)
            elif x=="l":
                uj+=str(21)
            elif x=="m":
                uj+=str(22)
            elif x=="n":
                uj+=str(23)
            elif x=="o":
                uj+=str(24)
            elif x=="p":
                uj+=str(25)
            elif x=="q":
                uj+=str(26)
            elif x=="r":
                uj+=str(27)
            elif x=="s":
                uj+=str(28)
            elif x=="t":
                uj+=str(29)
            elif x=="u":
                uj+=str(30)
            elif x=="v":
                uj+=str(31)
            elif x=="w":
                uj+=str(32)
            elif x=="x":
                uj+=str(33)
            elif x=="y":
                uj+=str(34)
            elif x=="z":
                uj+=str(35)


    if int(uj)%97==1:
        print("Lehetséges IBAN szám")
    else:
        print("Nope")

else:
    print("Hibás IBAN szám! Nem megfelelő számú karakter!")
