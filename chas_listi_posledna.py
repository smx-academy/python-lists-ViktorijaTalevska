#Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na otceni za nekoj
#ucenik, da se presmeta prosek za ucenik i da se proveri koja otcena najveke e zastapena

oceni=[]
while True:
 ocena=input("Vnesete ocena:(izberi stop dokolku sakate da prestanete)\n")
 if ocena=="stop":
    break
 oceni.append(ocena)
print(oceni)
dolzhina=len(oceni)
vkupno=sum(oceni)
prosek=vkupno/dolzhina
print("Sreden prosek na vashite oceni iznesuva:{}\n".format(prosek))
eden=oceni.count(1)
dva=oceni.count(2)
tri=oceni.count(3)
cheteri=oceni.count(4)
pet=oceni.count(5)

