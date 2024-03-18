def tantargy(_sorak):
    _jegyek=""
    for i in _sorak:
        a = input("Kérem adja meg a "+ i +"jegyét:")
        while int(a)<1 or int(a)>5:
            a=input("Kérem adja meg a "+ i +"jegyét helyesen: ")
        _jegyek+="*"+a
    return _jegyek

def beker(fajl,mod="w", szam=3, sorak=[]):
    jegyek=""
    with open(fajl, mod, encoding="utf-8") as cel:
        for i in range(szam):
            _nev=input("Kérem adja meg a nevét: ")
            jegyek=tantargy(sorak)
            cel.write(_nev+jegyek+"\n")

def beolvas(fajl,jel):
    with open(fajl,'r',encoding='utf-8') as forras:
        _adatok=[]
        for sor in forras:
            egy=sor.strip().split(jel)
            _adatok.append(egy)
        return _adatok

def atlag(_adat):
    osszeg=0
    for i in range(1,len(_adat)):
        osszeg+=int(_adat[i])
    return osszeg/(len(_adat)-1)
def atlag_tantargy(_adatok,_i):
    osszeg=0
    for egy in _adatok:
        osszeg+=int(egy[_i])
    return osszeg/(len(_adatok))


orak=["matek","magyar","prg","töri","angol"]
beker('jegyek.csv',"w+",int(input("Kérem adja meg hanyszor:")),orak)
adatok=beolvas("jegyek.csv", "*")
print(adatok)
for egy_adat in adatok:
    print(egy_adat[0], atlag(egy_adat))
for i in range(len(orak)):
    print(orak[i],"átlag: ",atlag_tantargy(adatok, i+1))



#########legtöbb ötös
#########második legjobb átlag
#########nevek abc sorrendbe
#########legkevesebb bukás
#########mennyi az összes bukás