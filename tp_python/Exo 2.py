def maximum(n1,n2,n3,n4):
    maxi=n1
    if n2>n1:
        maxi=n2
    if n3>maxi:
        maxi=n3
    if n4>maxi:
        maxi=n4
    return maxi 
n1=int(input("entrez n1:"))
n2=int(input("entrez n2:")) 
n3=int(input("entrez n3:"))
n4=int(input("entrez n4:"))
print("Le maximum est:",maximum(n1,n2,n3,n4))