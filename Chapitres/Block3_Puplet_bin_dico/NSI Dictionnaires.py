from math import*
from turtle import*
from random import*

#ex2TP
T=[1,3,2,1,4,1,2,1,5]
def occurence(T):
    d={}
    for i in range (len(T)):
        if T[i] in d:
            d[T[i]]+=1
        else:
            d[T[i]]=1
    return d

f=open("ltdme80j-p.txt")
text=f.read().split()
f.close()

d=occurence(text)

#ex3TP
def plusfrequent(d,k):
    maxi=0
    for e in d :
        if len(e)==k and d[e]>maxi:
            maxi=d[e]
            res=e
    return res

#ex4TP
def compare_tableaux(t,u):
    if t==u:
        res=True
    return res

#ex6TP:
vente={"Durant":13,"Dupont":15,"Dupond":17,"Durand":20}
def nbrventes(vente):
    tot=0
    for e in vente:
        tot=tot+vente[e]
    return tot
def meilleurvendeur(vente):
    m=0
    for r in vente:
        if vente[e]>= m:
            m=vente[e]
            res=e
    return res

#ex7TP
notes={"Tom":[8,10,12],"Mila":[9,10],"Alex":[],"Lina":[12,10,8]}


    
    

