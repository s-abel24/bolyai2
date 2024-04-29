# #Be: Játékosok neve
# 	Hány kör lesz.
# 3 dobókockával dobunk, az nyer akinél a dobókockák összege a legnagyobb.
# Ki:melyik kört ki nyerte
# 	ki nyert leggyakrabban
# 	Mennyi körönként a dobások átlaga
# 	A nyertesek abc sorrendben.Fáljba kiírni.



#
# import random as r
#
# Anna = 0
# Peter = 0
# for i in range():
#
# for i in range(dobas):
#     Aveletlen = (r.randint(1, 6)) + (r.randint(1, 6)) + (r.randint(1, 6))
#     Pveletlen = (r.randint(1, 6)) + (r.randint(1, 6)) + (r.randint(1, 6))
#     if Aveletlen > Pveletlen:
#         print(round(Aveletlen, 1), round(Pveletlen, 1), "Anna nyert")
#     elif Aveletlen == Pveletlen:
#         print(round(Aveletlen, 1), round(Pveletlen, 1), "Döntetlen")
#     else:
#         print(round(Aveletlen, 1), round(Pveletlen, 1), "Péter nyert")

import random as r
def dobas(_szam): #3
    dobasok=[]
    for i in range(_szam):
        dobasok.append(r.randint(1,6))
    return dobasok #[1,4,6]
def osszeg(_dobasok): #[1,4,6]
    _osszeg=0
    for egy in _dobasok:
        _osszeg+=egy
    return _osszeg
def jatekosok():
    _nevek = []
    _nev = "asd"
    while _nev != "":
        _nev = input("Kérem adjon meg egy nevet: ")
        if _nev != "":
            _nevek.append(_nev)
    return _nevek


#*************************************************
nevek=jatekosok()
kor=int(input(("Hány kör lesz:")))
menet=[]
for nev in nevek:
    menet.append([nev,dobas,osszeg(3)])
max_menet[0]
for ertek in menet:
    if max[1]<ertek[1]
        max=ertek
print(max)
for nev in nevek:
    menet.append([nev, dobas(3)])

print(menet)