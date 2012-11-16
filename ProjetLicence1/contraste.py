
def contraste(t):
   minimum=255
   maximum=0
   for i in range (len(t)):
      for j in range (len(t[0])):
        if t[i][j]<minimum:
           minimum=t[i][j]
        if t[i][j]>maximum:
           maximum=t[i][j]
   for i in range (len(t)):
      for j in range(len(t[0])):
         t[i][j]=int(255.0/(maximum-minimum)*(t[i][j]-minimum)) #si minimum vaut 0 et maximum vaut 255, t[i][j] est conserve, et la fonction n'a plus d'effet
