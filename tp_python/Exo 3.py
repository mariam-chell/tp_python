from math import sqrt
a=int(input("entrez a:"))
b=int(input("entrez b:"))
c=int(input("entrez c:"))
if(a==0):
    if (b==0):
        if(c==0):
            S=("L'ensemble des nombres réels")
        else:
            S=("N'a pas de solutions")
    else:
        S=-c/b 
else:
    def Delta(a,b,c):
        Delta=b**2-4*a*c
        return(Delta(a,b,c))
    def resoudre(a,b,c):
        nbs=0
        x1=0
        x2=0
        if Delta>0:
            nbs=2
            x1=(-b-sqrt(Delta))/2*a
            x2=(-b+sqrt(Delta))/2*a
        elif Delta<0:
            nbs=0
        else:
            nbs=1
            x1=-b/2*a
        return nbs,x1,x2
    def afficher(nbs,x1,x2):
        if nbs==0:
            print("N'a pas de solutions")   
        elif nbs==1:
            print("La solution est:",x1)
        elif nbs==2:
            print( "Les solutions sont:",x1,x2)
        else:
            print("une infinité de solutions")


