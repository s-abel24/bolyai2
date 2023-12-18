# szamok=[]
# paros=[]
# paratlan=[]
# szam=int(input("kérek egy számot:"))
# while szam!=0:
#     szamok.append(szam)
#     szam = int(input("kérek egy számot:"))
# # print(szamok)
# for egy in szamok:
#     if egy%2==0:
#         paros.append(egy)
#     else:
#         paratlan.append(egy)
# print("teljes lista",szamok)
# print("páros",paros)
# print("páratlan",paratlan)
#szavak=[]
#rovid=[]
#hosszu=[]
#szo=(input("kérek egy számot:"))
#while szo!="":
#   szavak.append(szo)
#   szo=(input("kérek egy szót:"))
#for egy in szavak:
#    if len(egy)<6:
#       rovid.append(egy)
#    else:
#        hosszu.append(egy)
#print("teljes lista",szavak)
#print("páros",rovid)
#print("páratlan",hosszu)


#szo1 = input("Kérem, adjon meg egy szót:")
#szo2 = input("Kérem, adjon meg egy szót:")


#if "a" > "A":
#    print("szo1 nagyobb mint szo2")
#else:
#    print("nem nagyobb")
def kicsi(_szamok):
    _min=_szamok[0]
    for _szam in _szamok:
        if _min > _szam:
            _min = _szam
    return _min
def rendez(_lista):
    _rendez=[]
    while len(_lista) > 0:
        _rendez.append(kicsi(_lista))
        _lista.remove(kicsi(_lista))
    return _rendez
#*******************************
szamok=[34,11,3,13,5,9]
print(rendez(szamok))


