"""
Andrei primeste intr-o zi trei note, nu toate bune. Se hotaraste ca, daca ultima nota este cel putin 8, sa le spuna parintilor toate
notele primite iar daca este mai mica decat 8, sa le comunice doar cea mai mare nota dintre primele doua. Introduceti notele
luate si afisati notele pe care le va comunica parintilor. Exemple : Date de intrare 6 9 9 Date de iesire 6 9 9 ; Date de
intrare 8 5 7 Date de iesire 8.
"""
print("introdu notele(numere 1-10)")
n1=int(input("Prima nota"))
n2=int(input("A doua nota"))
n3=int(input("A treia nota"))
if n3>=8:
    print(n1,n2,n3,sep=" ")
elif n3<8:
    if n1>n2:
        print(n1)
    else: print(n2)