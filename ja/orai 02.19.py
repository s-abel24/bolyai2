# with open('eu.csv', 'r', encoding='utf-8') as forras:
#     forras.seek(0)
#     orszag=[]
#     varos =[]
#     ev =[]
#     for sor in forras:
#         a=(sor.strip().split(","))
#         orszag.append(a[0])
#         varos.append(a[1])
#         ev.append(int(a[2]))
#
# print("végén ez marad ",orszag)
# print("végén ez marad ",varos)
# print("végén ez marad ",ev)
#
# db=0
# for i in range(len(ev)):
#     if ev[i]==min(ev):
#         db+=1
#         print(orszag[i])
# print(db)
#
# for i in range(len(varos)):
#     if varos[i][0]=="B":
#         db+=1
#         print(orszag[i],"-",varos[i])
#
# rovid=len(orszag[0])
# index=0
# for i in range(len(ev)):
#     if len(orszag[i])<rovid:
#         rovid=len(orszag[i])
# for i in orszag:
#     if len(i)==rovid:
#         print("legrövidebb:",i)
#
# for i in orszag:
#     if len(i)>6:
#         print("6-nál hosszabb név:",i)

   # print(forras.readline())
   # print(forras.seek(0))
   # print(forras.readline())
   # print(forras.tell())

with open('parduc.txt', 'r', encoding='utf-8') as forras:
        forras.seek(0)
        for sor in forras:
            print(sor)

szoveg=[]
    for sor in forras: