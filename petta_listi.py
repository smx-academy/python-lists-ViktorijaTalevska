#Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi,
#  da se dodadat vo lista i da se najde vtoriot najgolem broj

lista=[]
lista2=[]
while True:
 broj=input("Vnesete broj: (napishi stop za da prestanete)\n")
 if broj=="stop":
    break
 lista.append(int(broj))
print(lista)
lista2=lista.copy()#pram kopija od prvata niza
max1=max(lista)
lista2.remove(max1)#go otstranuvam najgolemiot chlen
max2=max(lista2)#ova vsushnost e vtoriot najgolem chlen
print("Najgolem vtor broj e:{}".format(max2))