#def felvaltva(string1, string2):
#    hosszabb = max(len(string1), len(string2))
#    eredmeny = ""

#    for i in range(hosszabb):
#        if i < len(string1):
#            eredmeny += string1[i]
#        if i < len(string2):
#            eredmeny += string2[i]
#   return eredmeny


#string1 = input("Kérd be az első stringet: ")
#string2 = input("Kérd be az első stringet: ")


#eredmeny = felvaltva(string1, string2)
#print(eredmeny)

# #3.feladat
#  szo = input("Kérem a szót:")
#  nagyszo=""
#  for betu in szo:
#      nagy=ord(betu)
#      if nagy >96 and nagy <123:
#          nagy-=32
#          betu=chr(nagy)
#      nagyszo+=betu
#  hossz=len(nagyszo)
#  ford=""
#  for i in range(hossz-1,-1,-1):
#      ford+=nagyszo[i]
#  print(ford)
#  szo=input("Kérem a mondatot:")
#  szunet=[]
#
#  for i in range(len(szo)):
#      if szo[i]==" ":
#          szunet.append(i)
#
#  elozo=0
#  for i in szunet:
#      b=ord(szo[elozo:i][0])
#     if b >96 and b <123:
#          b-=32
#      print(chr(b)+szo[elozo+1:i])
#      elozo=i+1

#1c
# szo=input("Kérem a szót:")
# for betu in szo:
#     print(ord(betu))
#     print(chr(9))
#2ab
 szo=input("Kérem a szót:")
 hossz=len(szo)
 szof=""

 for betu in range(hossz-1, -1, -1) :

     szof+=szo[betu]
 if szo==szof:
     print("a szó palindrom")
 else:
     print("nem palindrom")


