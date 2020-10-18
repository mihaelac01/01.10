"""
cunoscand data curenta exprimata prin trei numere intregi reprezentand anul,luna,ziua precum si data nasterii unei persoane, 
exprimata la fel, sa se faca un program care sa calculeze varsta persoanei respective in numar de ani impliniti. Exemplu: 
Date de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de iesire 44 ani.
"""
ac=int(input("Anul curent"))
zc=int(input("Ziua curenta"))
lc=int(input("Luna curenta"))
an=int(input("Anul nasterii"))
zn=int(input("Ziua nasterii"))
ln=int(input("Luna nasterii"))
if lc==ln:
    if ((zn>zc)or(zc==zn)):
        print((ac-an)+1,"ani")
    else:
        print(ac-an,"ani")
    elif lc>ln:
        print((ac-an)+1,"ani")
    else:
        print(ac-an,"ani")