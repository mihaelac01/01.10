"""
se considera trei numere intregi. Daca toate sunt pozitive, sa se afiseze numarul mai mare dintre al doilea si al treilea numar,in
caz contrar sa se calculeze suma primelor doua numere. Exemple: Date de intrare 45 23 100 date de iesire 100 ; Date de
intrare 34 -25 10 Date de iesire 9.
"""
a=int(input("primul numar"))
b=int(input("al doilea numar"))
c=int(input("al treilea numar"))
if((a>=0)and(b>=0)and(c>=0)):
    if b>c:
        print(b)
    else:
        print(c)
else: print(a+b)