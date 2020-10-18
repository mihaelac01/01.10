"""
La un concurs se dau ca premii primilor 100 de concurenti, tricouri de culoare alba,rosie,albastra si neagra,in aceasta
secventa.Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu: date de intrare: x=38 date de iesire: rosie
"""
x=int(input("Locul ocupat de Ionel"))
if x>100:
    print("Nu primeste tricou")
elif x%4==0:
    print("alba")
elif x%4==1:
    print("rosie")
elif x%4==2:
    print("albastru")
else:
    print("neagra")