def triInsertion (t):
    for i in range (1,len(t)):
        tmp=t[i]
        j=i-1
        while j>-1 and t[j]>tmp:
            t[j+1]=t[j]
            j-=1
        t[j+1]=tmp
    return t

def filtrage (t):
    suite=[]
    for i in range (1,len(t)-1):
        for j in range (1,len(t[0])-1):
            suite+=[t[i-1][j-1]]+[t[i-1][j]]+[t[i-1][j+1]]+[t[i][j-1]]+[t[i][j+1]]+[t[i+1][j-1]]+[t[i+1][j]]+[t[i+1][j+1]]
            triInsertion(suite)
            t[i][j]=suite[4]
            suite=[]

