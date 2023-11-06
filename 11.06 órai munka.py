gyumolcs=["alma","körte","banán","szilva","narancs","áfonya","barack"]
print(gyumolcs[4])
print(len(gyumolcs))
hossz=len(gyumolcs)

for i in range(hossz):
    print(gyumolcs[i])

for elem in gyumolcs:
    print(elem)

foglalkozasok = ['postás', 'rendőr', 'villanyszerelő',
'a szomszéd', 'gázos', 'díjbeszedő', 'handlé', 'szódás', 'képkereskedő', 'a házmester',
'a fia', 'kéményseprő']




listam=['hétfő ', 'kedd', 'szerda', 'Július', 'csütörtök', 'péntek']
listam.append('szombat')
listam.insert(1,"narancs")
print(listam)

del(listam[4])
print(listam)

szamok = [17, 38, 10, 25, 72]
szamok.sort()
[10, 17, 25,38, 72]
