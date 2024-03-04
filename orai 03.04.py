# with open("szamok.txt", 'w', encoding="utf-8") as cel:
#     for i in range(5):
#       cel.write(input("Kérem adja meg a "+str(i+1)+". számot")+"\n")
#
# with open("szamok.txt", 'r', encoding="utf-8") as cel:
#     osszeg=0
#     for sor in cel:
#         osszeg+=int(sor.strip())
# print(f'szamok.txt fáljban lévő számok összege: {osszeg}')

def beker():
    with open("adatok.csv", 'w', encoding="utf-8") as cel:
        sor='1'
        while sor!=" ":
            sor=input("Kérem adja meg a nevét:")
            cel.write(sor)
            if sor !="":
                cel.write(";"+input("Kérem adja meg a szül.évet:")+"\n")


with open("adatok.csv", 'r', encoding="utf-8") as forras:
    adatok=[]
    for sor in forras:
        egy=sor.strip().split(";")
        adatok.append(egy)
    print(adatok)

for egy in adatok:
    print(egy[0],"--->",2024-int(egy[1]))

