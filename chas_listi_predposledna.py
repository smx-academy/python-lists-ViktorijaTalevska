#Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, da se proveri dali
#brojot e pogolem ili pomal od 100 i da se dodade vo lista so broevi pomali ili pogolemi od 100.
#Potoa da se proveri dolzinata na listite, ako lsitata so broevi pogolemi od 100 ima neparen broj
#elementi da se izbrise posledniot za da ima paren broj, a listata so pogolemi od 100 ako ima
#paren broj elementi da se izbrise prviot za da ima neparen broj elementi

pogolemi=[]
pomali=[]
for i in range(10):
 broj=int(input("Vnesete broj:\n"))
 if broj>100:
    pogolemi.append(broj)
 else:
    pomali.append(broj)
print(pogolemi)
print(pomali)
dolzhina1=len(pogolemi)
dolzhina2=len(pomali)
print("Prvata lista sodrzhi {} elementi, dodeka vtorata lista sodrzhi {} elementi".format(dolzhina1,dolzhina2))
if dolzhina1%2!=0:
    pogolemi.pop()
    print(pogolemi)
else:
    pogolemi.pop(0)
    print(pogolemi)
    
