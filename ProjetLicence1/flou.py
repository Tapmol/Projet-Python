def floutage(t):
    somme=0
    moyenne=0
    for i in range (1,len(t)-1):
        for j in range (1, len(t[0])-1):
#on fait la somme des cases au voisinage de t[i][j] 
            somme=t[i-1][j-1]+ t[i-1][j]+t[i-1][j+1]+t[i][j-1]+t[i][j+1]+t[i+1][j-1]+t[i+1][j]+t[i+1][j+1]
            moyenne=somme//8
            t[i][j]=moyenne
