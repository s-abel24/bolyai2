#szamok = [17, 38, 10, 25, 72]

#print(szamok.index(17))
#szamok.sort()


#print(szamok.index(17))

szavak = ['sonka', 'sajt', 'lekvár', 'csokoládé']
szavak[2:2] =["méz"]
print(szavak)
szavak[5:5] =['kolbász', 'ketchup']
print(szavak)
szavak[2:5] = []
print(szavak)

listam= [10, 1, 8, 3, 5]
total = 0
for i in range(len(listam)):
    total += listam[i]
print(total)

listam=[]

szam=1
while szam!=0:
    szam=int(input("Írd be az egy egész számot!"))