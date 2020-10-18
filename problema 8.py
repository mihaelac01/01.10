"""
sa se afiseze cel mai mare numar par dintre doua numere introduse in calculator. Exemple : Date de intrare 23 45 Date de
iesire nu exista numar par; Date de intrare 28 14 Date de iesire 28; Date de intrare 77 4 Date de iesire 4
"""
a=int(input("primul numar"))
b=int(input("al doilea numar"))
if((a%2==0)and(b%2==0)):
    if a>b:
        print(a)
    else:
        print(b)
elif ((a%2==0)and(b%2==0)):
    print(a)
elif((a%2!=0)and(b%2==0)):
    print(b)
else:
    print("nici unul dintre numere nu e par")