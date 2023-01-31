#Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, 
# da se dodadat vo lista, i da se najde najdolgoto ime

iminja=[]
while True:
 ime=(input("Vnesete ime (napishete stop dokolu sakate da prestanite)\n"))
 if ime=="stop":
    break
 iminja.append(ime)
print(iminja)
lista=[] #si pram edna lista so dolzhini
for ime in iminja:
 dolzhina=len(ime)
 lista.append(dolzhina)
najgolemo=max(lista)
index=lista.index(najgolemo) #go naogam indeksot od vtorata lista so dolzhini koj sho element e najgolem
print(iminja[index]) #istiot indeks go printam od prvata lista bidejki e imeto so najgolema dolzhina
