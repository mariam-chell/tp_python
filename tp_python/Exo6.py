def present(L,x):
    i=0
    while i<len(L):
        if([i]==x):
            return True
        i=i+1
    return False
x=float(input("entrez x:"))
print("La fonction est:",present([1,2,3,4],x))