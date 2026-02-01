def sans_doublons(L):
    R=[]
    for i in range(len(L)):
        if not present(R,L[i]):
            R.append(L[i])
    return R