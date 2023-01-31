#Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, 
# da se ispecati listata i korisnikot da moze da izbere kolku elementi i koi elementi ke gi izbrise

lista=[]
while True:
 broj=input("Vnesete broj: (ili izberete stop dokolku sakate da prestanite)\n")
 if broj=='stop':
    break
 lista.append(int(broj))
print(lista)
print("Izberete kolku elementi sakate da izbrishete")
kolku=int(input())
for i in range(kolku):
    koj=int(input("Koj broj sakate da go izbrishete"))
    lista.remove(koj)
print(lista)

    