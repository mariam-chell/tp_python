def Ind_PG_I(L,I):
    if I>len(I):
        I=len(L)
    ind=0
    for i in range(I):
        if(L[i]>L[ind]):
            ind=I
    return ind
def trier(L):
    I=len(L)
    while I>1:
        ind=Ind_PG_I(L,I)
        tmp=L[ind]
        L[ind]=L[I-1]
        L[I-1]=tmp
        I=I-1
    return ind
Ind_PG_I([1,2,3],6)
trier([1,2,3])
