def luminosite (t,valeur):
    for i in range (len(t)):
        for j in range (len(t[0])):
            t[i][j]+=valeur
            if t[i][j]>255:
                t[i][j]=255
            if t[i][j]<0:
                t[i][j]=0
            
