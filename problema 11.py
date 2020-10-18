"""
Se dau trei numere. Sa se afiseze aceste numere unul sub altul, afisand in dreptul fiecaruia unui dintre cuvintele PAR sau IMPAR . 
Exemplu: Date de intrare: 45 3 24 Date de iesire : 45 impar 3 impar 24 par
"""
a=int(input("primul numar"))
b=int(input("al doilea numar"))
c=int(input("al treilea numar"))
if ((a%2==0)and(b%2==0)and(c%2==0)):
    print(a,"PAR")
    print(b,"PAR")
    print(c,"PAR")
elif ((a%2==0)and(b%2==0)and(c%2!=0)):
    print(a,"PAR")
    print(b,"PAR")
    print(c,"IMPAR")
elif ((a%2==0)and(b%2!=0)and(c%2==0)):
    print(a,"PAR")
    print(b,"IMPAR")
    print(c,"PAR")
elif ((a%2!=0)and(b%2==0)and(c%2==0)):
    print(a,"IMPAR")
    print(b,"PAR")
    print(c,"PAR")
elif ((a%2!=0)and(b%2!=0)and(c%2==0)):
    print(a,"IMPAR")
    print(b,"IMPAR")
    print(c,"PAR")
elif ((a%2==0)and(b%2!=0)and(c%2!=0)):
    print(a,"PAR")
    print(b,"IMPAR")
    print(c,"IMPAR")
elif ((a%2!=0)and(b%2==0)and(c%2!=0)):
    print(a,"IMPAR")
    print(b,"PAR")
    print(c,"IMPAR")
else:
    print(a,"IMPAR")
    print(b,"IMPAR")
    print(c,"IMPAR")