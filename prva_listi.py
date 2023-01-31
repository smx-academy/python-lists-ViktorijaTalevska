#.Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi,
#  da se dodadat vo list i da se soberat site broevi vo listata

lista=[]
for i in range(10):
    broj=int(input("Vnesete broj"))
    lista.append(broj)
print(lista)
zbir=sum(lista)
print("Zbirot na site elementi vo listata iznesuva:{}".format(zbir))

