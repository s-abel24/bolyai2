#szoveg=input("Kérem ....")
#adatok=[]
#szamok=[]
#szavak=[]
#while szoveg!="":
#    adatok.append(szoveg)
#    szoveg=input("Kérem ....")
#print(adatok)
#for egy in adatok:
#    szam=True
#    for betu in egy:
#        if betu not in "0123456789":
#            szam=False
#    if szam:
#       szamok.append(egy)
#    else:
#        szavak.append(egy)
#print(szamok)
#print(szavak)


szamok=[]
harom=[]
nemharom=[]

for i in range(6):
    #szamok.append(int(input("Kérem .....")
    szam=int(input("Kérem...."))
    szamok.append(szam)

print(szamok)
for egy in szamok:
    if egy%3==0:
        harom.append(egy)
    else:
        nemharom.append(egy)
print(harom)
print(nemharom)