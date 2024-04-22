# import math
# print(math.sin(math.pi/2))
# pi=25
# Pi=math.pi
# print("sajat pi:",pi)
# print("Nem sajat pi:",Pi)
# print(3+Pi)
# print(3+pi)
#
# for name in dir(math):
#     print(name,end="\t")

# import random
# for name in dir(random):
#     print(name,end="\t")

# import random as r
# szam=input("Kérek egy számot!")
# fejsz=0
# irassz=0
# for i in range(1,szam):
#     veletlen=r.random()
#     if veletlen>0.5:
#         print(str(i+1)+". Fej")
#     else:
#         print(str(i+1)+". Írás")

import random as r
lista=["kacsa","liba","tyúk","csirke","pipi","kakas"]
szo=(r.choice(lista))
for i in range(len(szo)):
    print(".",end="")

betu=(input("adjon meg egy betűt:"))



