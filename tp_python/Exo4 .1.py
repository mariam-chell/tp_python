def Seuil():
    m=0
    v=57
    while(v<200):
        v=v*103
        m+=1
    return m
print("le nombre de mois est:",Seuil())