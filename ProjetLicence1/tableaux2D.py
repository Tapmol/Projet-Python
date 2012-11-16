def creer_tableau_1D(l, val):
    t=[val]*l
    return t

def copier_tableau_1D(t1,t2):
    for i in range (len(t1)):
        t2[i]=t1[i]

def creer_tableau(h,l,val):
    t=creer_tableau_1D(h,None)
    for i in range (h):
        t[i]=creer_tableau_1D(l,val)
    return t

def copier_tableau (t1,t2):
    for i in range (len(t1)):
        for j in range (len(t1[0])):
            t2[i][j]=t1[i][j]
        


                    
                    
