# def teglalap(a, b):
#     terulet = a * b
#     return terulet
#
# a = int(input("Kérem az 'A' oldalt!"))
# b = int(input("Kérem a 'B' oldalt"))
# terulet = teglalap(a, b)
# print("A téglalap területe:", terulet)

# def legnagyobb_kozos_oszto(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# # Teszteljük a függvényt
# szam1 = int(input("Kérem adjon meg egy szamot!"))
# szam2 = int(input("Kérem adja meg a második számot!"))
# print(f"A(z) {szam1} és {szam2} legnagyobb közös osztója: {legnagyobb_kozos_oszto(szam1, szam2)}")

# def osztok(szam):
#     osztoszam = 0
#     for i in range(1, szam + 1):
#         if szam % i == 0:
#             osztoszam += 1
#     return osztoszam
#
#
# szam = int(input("Kérem a számot!"))
# print(f"A(z) {szam} számnak {osztok(szam)} osztója van.")

def szamolas(lista, érték):
    szam = 0
    for item in lista:
        if item == érték:
            szam += 1
    return szam

lista = [1, 2, 3, 4, 4, 5, 4, 6, 4]
ertekszam = int(input("Kérem adja meg az értéket:"))
eredmeny = szamolas(lista, ertekszam)
print(f"A(z) {ertekszam} érték {eredmeny} alkalommal szerepel a listában.")
