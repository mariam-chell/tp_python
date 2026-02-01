def generalisation(vi,vf,taux):
    m=0
    v=vi
    while(v<vf):
        v=v+taux*v
        m+=1
    return m
v=float(input("entrez v:"))
vf=float(input("entrez vf:"))
taux=float(input("entrez taux:"))
print("La generalisation est:",generalisation(1,2,3))