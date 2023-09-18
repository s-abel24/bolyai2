magassag = float(input("Kérem, adja meg a magasságát m-ben: "))
kg = float(input("Kérem, adja meg a tömegét kg-ban: "))
bmi = kg / (magassag ** 2)
bmiveg = round(bmi, 2)
alsohatar = 18.5 * (magassag ** 2)
alsoveg = round(alsohatar, 2)
felsohatar = 24.9 * (magassag ** 2)
felsoveg = round(felsohatar, 2)
print(35 * "*", 5 * "-", 35 * "*", sep="")
print(f"Az ön testtömegindexe: {bmiveg} %")
print(f"Az ön magasságához az ideális testtömeg: {alsoveg} kg és {felsoveg} kg között van")
if bmiveg <= 16:
    print("Súlyos soványság")
elif  16 < bmiveg <= 17:
        print("Mérsékelt soványság")
elif 17 < bmiveg <= 19:
        print("Mérsékelt soványság")
elif 19 < bmiveg <= 25:
        print("Normális testsúly")
elif 25 < bmiveg <= 30:
        print("Túlsúlyos")
elif 30 < bmiveg <= 35:
        print("I. fokú elhízás")
elif 35 < bmiveg <= 40:
        print("II. fokú elhízás")
if bmiveg >= 40:
    print("III. fokú (súlyos) elhízás")




