#exemple
T=[1,2,4,7,13,27,42,64,101]
def treeve(x,T):
    b=False 
    for i in range(len(T)):
        if x==T[i]:
            b=True
    return b
print (treeve(304,T))

def recherche(tab,val):
    res=-1
    for i in range (len(tab)):
        if tab[i]==val:
            res=i
    return res 

def recherche_dichotomique(tab,val):
    res=-1
    gauche=0
    droite=len(tab)-1
    while ...... and res=-1:
        milieu=(gauche+droite)//2
        if tab[milieu]=val:
            res=milieu
        elif tab[milieu]>val:
            droite = milieu-1


