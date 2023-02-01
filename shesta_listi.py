#Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. 
# Korisnikot da moze da vnesuva produkti se dodeka ne izbere deka saka da plati. 
# Produktitte da se dodavaat vo edna lista, cenite vo druga lista.
#  Koga ke izbere deka saka da plati da mu se ispecatat produktite 
# i cenite vo nalik na "fiskalna smetka". 
# Da ima moznost korisnikot da plati i da se presmeta dali i kolku treba da mu se vrati kusur

produkti=[]
ceni=[]
while True:
 produkt=input("Vnesi ime na produkt: (izberi plati dokolku sakash da platish)\n")
 if produkt=="plati":
  break
 cena=int(input("Vnesi cena na produkt:\n"))
 produkti.append(produkt)
 ceni.append(cena)
gotovina=sum(ceni)
vkupno=len(produkti)
print("Ime na produkt:   Cena:")
for i in range(vkupno):
 print("{}   {}denari".format(produkti[i],ceni[i]))
print("Vkupno:{}".format(gotovina))
kesh=int(input("Vnesete kolku kesh imate:\n"))
if kesh-gotovina>0:
 print("Za vrakanje imate kusur od:{}\n".format(kesh-gotovina))
elif kesh-gotovina==0:
 print("Vi blagodarime")
else:
 print("Imate greshka")