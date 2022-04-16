from math import*
clavier=(('1','2','3'),('4','5','6'),('7','8','9'),('*','0','#'))

def inverseclavier(clavier):
    x={"#":(),'0':(),'*':(),'9':(),'8':(),'7':(),
        '6':(),'5':(),'4':(),'3':(),'2':(),'1':()}
    for i in range (len(clavier)):
        for j in range(len(clavier[0])):
            n=clavier[i][j]
            x[n]=(i,j)
    return x

def distancetouches(a,b,coord):
    A=coord[str(a)]
    B=coord[str(b)]
    dist=sqrt((N[0]-M[0])**2+(N[1]-M[1])**2)
    return dist 
    
    
    
    
