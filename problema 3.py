"""
Sa se verifice daca o litera introdusa este vocala sau consoana. Exemplu: Date de intrare a Date de iesire vocala.
"""
l=input("Litera")
if((l="a")or(l="e")or(l="i")or(l="o")or(l="u")or(l="ă")or(l="î")):
    print("vocala")
else:
    print("consoana")