"""
se introduc varstele a 3 persoane. Aflati varstele cuprinse intre 18 si 60 de ani. Exemplu: Date de intrare 56 34 12 Date de iesire 56 34
"""
a=int(input("varsta primei persoane"))
b=int(input("varsta a doua persoana"))
c=int(input("varsta a treia persoana"))
if ((a>18)and(a<60)):
    print(a)
elif ((b>18)and(b<60)):
    print(b)
else:
    print(c)