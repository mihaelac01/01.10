"""
Se introduc trei date de forma numar curent elev,punctaj.Afisati numarul elevului cu cel mai mare punctaj.Exemplu:Date de intrare 
nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de iesire punctaj maxim are elevul cu nr crt 7.
"""
n1=int(input("numarul primului elev"))
n2=int(input("numarul al doilea elev"))
n3=int(input("numarul al treilea elev"))
p1=int(input("punctajul primului elev"))
p2=int(input("punctajul al doilea elev"))
p3=int(input("punctajul al treilea elev"))
if ((p1>p2)and(p1>p3)):
    print("Punctajul maxim are elevul cu numarul",n1)
elif ((p2>p1)and(p2>p3)):
    print("Punctajul maxim are elevul cu numarul",n2)  
elif ((p3>p1)and(p3>p2)):
    print("Punctajul mare are elevul cu numarul",n3)  
elif ((p1==p2)and(p1>p3)and(p2>p3)):
    print(n1,n2,"au punctaj egal")
elif ((p1==p3)and(p1>p2)and(p3>p2)):
    print(n1,n3,"au punctaj egal")
elif ((p2==p3)and(p2>p1)and(p3>p1)):
    print(n1,n3,"au punctaj egal")
else:
    print("toti au acelasi punctaj")