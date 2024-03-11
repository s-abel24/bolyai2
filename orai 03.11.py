def beker(falj,mod="w",szam=3):
    with open(falj,"w",encoding="utf-8") as cel:

        for i in range(szam):
            nev = input("Kérem adja meg a nevét:")
            osszpont = input("Kérem adja meg az összpontszámot:")
            pontszam = input("Kérem adja meg a pontszámát:")
            cel.write(nev+";"+osszpont+";"+pontszam+"\n")
def beolvas(falj,jel):
    with open(falj,"r",encoding="utf-8") as forras:
        _adatok=[]
        for sor in forras:
            egy=sor.strip().split(jel)
            _adatok.append(egy)
    return _adatok
def szazalek(lista):
    nev=lista[0]
    ossz=int(lista[1])
    pont=int(lista[2])
    print(nev,"-",round(pont/ossz*100,1),"%")
#print(lista[0],"-",round(int(lista[2])/int(lista[1])*100,2),"%")
def atlag(losztaly):
    ossz=0
    spont=0
    for egy in losztaly:
        ossz+=int(egy[1])
        spont+=int(egy[2])
    print(spont)
    print("Az átlageredmény:",(round(spont/ossz*100)),"%")


#----------------------------------------------
beker('pontok.csv','a+',int(input("Kérem adja meg hányszor.... ")))
adatok=beolvas("pontok.csv",";")
print(adatok)
for egy_adat in adatok:
    szazalek(egy_adat)
atlag(adatok)



