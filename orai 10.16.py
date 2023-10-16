osszeg=0
p=True
szam=int(input("Írj be egy pozitív egész számot:"))
while szam<2:

    szam=int(input("A szám nem megfelelő, Írj be egy pozitív egész számot:"))

for i in range(1, szam):
    if szam%i==0:
        #print('A',i,'osztója a',szam,'-nak.')
        osszeg+=i
        p=False

if osszeg==2*szam:
    print("A szám tökéletes", 2*szam)
else:
    print("Nem tökéletes a szám")




print("Osztóinak összege:", osszeg)
if p:
    print(f"A {szam} prímszám!")