def Insert(L,x):
    I=0
    while(x>L[I]):
        I=I+1
    L.Insert(I,x)
    return L
print("L'element:",Insert([1,2,3,4],2))
