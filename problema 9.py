"""
pe o masa de biliard sunt bile albe,rosii si verzi. Din fiecare culoare sunt bile de doua dimensiuni: mari si mici. Sa se afiseze
cate bile sunt in total pe masa de biliard. Un jucator vrea sa-i spuneti cate bile sunt mai multe, cele mici sau cele mari, afisand
numarul lor. De ce culoare sunt bilele cele mai numeroase? Precizati numarul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
Nr. bile albe mari 3....
"""
xa=int(input("Numarul de bile albe mici"))
xr=int(input("Numarul de bile rosii mici"))
xv=int(input("Numarul de bile verzi mici"))
ya=int(input("Numarul de bile albe mari"))
yr=int(input("Numarul de bile rosii mari"))
yv=int(input("Numarul de bile verzi mari"))
xt=xa+xr+xv
yt=ya+yr+yv
print("Sunt in total",xt+yt,"bile")
if xt>yt:
    print("Bile mici:",xt)
elif yt>xt:
    print("Bile mari:",yt)
else:
    print("Numarul de bile mici si numarul de bile mari sunt egale")
if ((xa+ya>xr+yr)and(xa+ya>xv+yv)):
    print("Bile albe:",xa+ya)
elif ((xr+yr>xa+ya)and(xr+yr>xv+yv)):
    print("Bile albe:",xr+yr)
elif ((xv+yv>xa+ya)and(xv+yv>xr+yr)):
    print("Bile albe:",xv+yv)
elif ((xa+ya==xr+yr)and(xr+yr>xv+yv)):
    print("Bile albe=Bile rosii:",xa+ya)
elif ((xr+yr==xv+yv)and(xr+yr>xa+ya)):
    print("Bile rosii=Bile verzi:",xr+yr)
elif ((xa+ya==xv+yv)and(xa+ya>xr+yr)):
    print("Bile albe=Bile rosii:",xa+ya)
else:
    print("Bile albe=Bile rosii=Bile verzi:",xa+ya)
