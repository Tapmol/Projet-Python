

def symetrie(t):
    i=0
    droite_verti_centree=len(t[0])//2
    while i<len(t):
        k=len(t[0])-1
        for j in range (droite_verti_centree):
            tmp=t[i][j]
            t[i][j]=t[i][k]
            t[i][k]=tmp
            k-=1
        i+=1
    return t
