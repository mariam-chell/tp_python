def Lesindices(L,x):
    R=[]
    i=0
    while i<len(L):
        if x==L[i]:
            R.append(i)
        i=i+1
    return R
print("Les indices de la liste sont:",Lesindices([1,2,3,4,5,6],6))