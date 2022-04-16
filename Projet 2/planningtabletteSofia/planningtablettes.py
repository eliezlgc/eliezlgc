import csv
import os as os
f1=open('C:\Users\PC\OneDrive - Région Île-de-France\Documents\Lycée\NSI\eliezlgc\Projet 2\planningtabletteSofia\planningtablettes.csv','r')
t1=list(csv.DictReader(f1,delimiter=","))
print(t1)
f1.close()

def tableau(t1):
    T=[""]*(len(t1)+1)
    T[0]="<tr>"+"<td>"+"Nom"+"</td>"+"<td>"+"Jour"+"</td>"+"<td>"+"Heure"+"</td>"+"<td>"+"Duree"+"</td>"+"</tr>"
    for i in range (len(t1)):
        T[i+1]= T[i+1]+"<tr>"
        for cle in t1[i]:
            T[i+1]= T[i+1]+"<td>"+t1[i][cle]+"</td>"
        T[i+1]= T[i+1]+"</tr>"
    return T

T=tableau(t1)
print(T)


f=open("tab_planning.html","w")
f.writelines(["<!DOCTYPE html>\n","<html>\n","<body>\n","<table>\n"])
f.writelines(T)
f.writelines(["</table>\n"])

D={"8h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"9h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"10h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"11h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"12h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"13h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"14h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"15h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"16h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"17h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0},"18h":{"Lundi":0,"Mardi":0,"Mercredi":0,"Jeudi":0,"Vendredi":0}}


def parcours(t1):
    for i in range(len(t1)):
        j=t1[i]["Jour"]
        print(j)
        h=t1[i]["Heure"]
        print(h)
        D[h][j]+=1
    return D
print(parcours(t1))


def edt(D):
    Z=[""]*(len(D)+1)
    Z[0]="<tr>"+"<td>"+"Heure"+"</td>"+"<td>"+"Lundi"+"</td>"+"<td>"+"Mardi"+"</td>"+"<td>"+"Mercredi"+"</td>"+"<td>"+"Jeudi"+"</td>"+"<td>"+"Vendredi"+"</td>"+"</tr>"
    for i in range (len(D)):
        Z[i+1]= Z[i+1]+"<tr>"
        for cle in D[str(i+8)+"h"]:
            Z[i+1]= Z[str(i+1) ]+"<td>"+D[str(i+8)+"h"][cle]+"</td>"
        Z[i+1]= Z[i+1]+"</tr>"
    return Z
print(edt(D))
