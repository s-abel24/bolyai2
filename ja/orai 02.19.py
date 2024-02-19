with open('eu.csv', 'r', encoding='utf-8') as forras:
    forras.seek(0)
    for sor in forras:
        print(sor.strip().split(",")[2])


   # print(forras.readline())
   # print(forras.seek(0))
   # print(forras.readline())
   # print(forras.tell())

