#Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, 
# da se dodadat vo lista i da se najde najgolemiot broj

lista=[]
while True:
 broj=input("Vnesete broj: (ili izberete stop dokolku sakate da prestanite)")
 if broj=='stop':
    break
 lista.append(int(broj))

print(lista)
najgolem=max(lista)
print("Najgolem e brojot:{}".format(najgolem))
