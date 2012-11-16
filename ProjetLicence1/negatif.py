def negatif(t):
    for i in range (len(t)):
        for j in range (len(t[0])):
            t[i][j]=255-t[i][j]
    
