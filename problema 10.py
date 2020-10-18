"""
La ferma de gaini copanul este democratie. Fiecare gaina primeste exact acelasi numar de boabe de porumb. Cele care nu pot
fi impartite vor fi primite de curcanul Clapon. Sa se spuna cine a primit mai multe boabe si cu cat.
Exemplu:Date de intrare 100 4050 Date de iesire: Curcanul mai mult cu 10 boabe.
"""
ng=int(input("Numarul de gaini"))
nb=int(input("Numarul total de boabe"))
nbg=nb//ng
nbc=nb-(ng*nbg)
if nbg>nbc:
    print("Gaina primeste mai mult cu",nbg-nbc,"boabe")
elif nbc>nbg:
    print("Curcanul primeste mai mult cu",nbc-nbg,"boabe")
else:
    print("Primesc acelasi numar de boabe")