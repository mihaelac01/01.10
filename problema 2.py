"""
La ora de matematica Gigel este scos la tabla. Profesoara ii dicteaza trei numere si ii cere sa verifice daca cele trei numere pot fi
laturile unui triunghi.Ajutati-l pe Gigel sa afle rezultatul. Scrieti un program care primeste numerele lui Gigel, care sunt mai mici
ca 32000, si returneaza DA sau NU. Observatie: Trei numere pot fi laturile unui triunghi numai daca fiecare este mai mic ca
suma celorlalte doua.Exemple: Date de intrare 3 5 7 Date de iesire Da Date de intrare 2 5 9 Date de iesire Nu.
"""
a=int(input("primul numar"))
b=int(input("al doilea numar"))
c=int(input("al treilea numar"))
if ((a<a+b)and(b<c+a)and(c<a+b)):
    print("Da")
else:
    print("Nu")