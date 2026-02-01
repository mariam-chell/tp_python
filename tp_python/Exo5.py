def somme(n):
    S=0
    while(n>0):
        r=n%10
        n=n//10
        S+=r
    return S
print("La somme est:",somme(1234))