"""
"Ma iubeste un pic, mult, cu pasiune, la nebunie, de loc, un pic,...". Rupand petalele unei margarete cu x petale, el(ea) ma
iubeste.... Exemplu: Date de intrare: x=10 Date de iesire... de loc.
"""
x=int(input("Numarul de petale"))
if x%6==0: print(" ma iubeste un pic ")
elif x%6==1:
    print("ma iubeste mult")
elif x%6==2:
    print("ma iubeste cu pasiune")
elif x%6==3:
    print("ma iubeste la nebunie")
elif x%6==4:
    print("ma iubeste de loc")
else:
    print("ma iubeste un pic")