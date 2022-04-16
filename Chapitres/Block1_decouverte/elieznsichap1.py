#ex8
Script 1


if 10**3<999 :
    print ("Ga")

if 6**2> 30 :
    print ("Bu")

if 10**3 or 6**2 >30 :
    print ("Zo")

#Script 2


if 10**3<999 :
    print ("Ga")
    if 6**2 > 30 :
        print ("Bu")

if 10**3 or 6**2 > 30 :
    print ("Zo")

#Script 3

if 10**3<999 :
  print ("Ga")
    if 6**2> 30 :
        print ("Bu")

    if 10**3 or 6**2 >30 :
        print ("Zo")


#Ex9

taille=float(input('entre ta taille en mètre'))
min=18.5*taille*taille
max=25*taille*taille
print("[",min,"]")

masse=float(input('entre ta masse'))
min= sqrt(masse/25)
max= sqrt(masse/18.5)
print("[",min,";",max,"]")


#ex10



#exemple cours boucle while

x=float(input('Entrer un réel: \n'))
i=0
s=x
while s>1:
    s=s/2
    i=i+1
print('Le logarithme entier',x,'est égal à',i)


#ex12

for i in range(2,5) :
	print(i**2)
	print(5//2) 

for i in range(2,5):
	print(i**2)
print(5//2)

i=4
while i>1 :
      print (i**2)
      i=i-1
      print (5//2)


i=4
while i>1 :
    print (i**2)
    i=i-1
print (5//2)

#ex13

for i in range (10,15):
    print ('Bonjour'+str(i))

##ex14

for i in range(10):
    print ('*')
    for j in range (10):
        print('*')

for i in range(10):
    for j in range(10):
        
#ex15

for m in range(1,11):
    print (m,"x",10,"=",m*10)
    m=+1

for m in range(1,11):
    for p in range (1,11):
        print (p,"x",m,"=",p*m)

#ex16
c=input("Nombre de clients à sonder")
for i in range (c):
    a=input("Quel est votre âge ?")
    n=input("Entrez votre nombre d'années d'études :")
    m=input("Etes vous en couple ou célibataire ?")
    e=input("Avez-vous des enfants ?")
#ex17
from math import*
from turtle import*
from random import*

n=int(input('on lance un dé d, \n\
Quel nombre de lancers sera nécessaire pour obtenir un 6 ?'))




#ex18
n=0
s=0
while n<100:
    n=n+2
    s=s+n
print ('La somme des entiers pairs inférieurs ou égaux a 100 est',s)
    

#ex19
n=int(input())
while n>0:
    n=n//10
   print (n)


n=int(input('entrez un entier positif'))
cpt=1
while n>=10:
    n=n/10
    cpt=cpt+1
print (cpt)

#ex19
floor c'est la partie entière
from math import *
n=int(input('Entrez un entier positif :'))
res=True
d=2
while d<floor(sqrt(n)):
    if n%d==0 :
        res = False
    d=d+1
print (res)    


#ex21
a-int(input('a-'))
b-int(input('b-'))
if a>0 and b>0 :
    m, n = a, b
    while m>-b :
        m, n=m-b, n+1
    print ('m=', mn 'n=', n)


#ex22
 quotien de par b :
a=int(input('a='))
b=int(input('b='))
cpt=0
while a>=b and b!=0:
    cpt+=1
    a=a-b, b
if b==0:
    print('Le dénominateur doit être non nul')
else:
    print(cpt)

#ex23
n=int(input('Entrez un entier : \n'))
i=1
s=0
while i<=n :
    z=i*i
    print('i=', i)
    print('z=', z)
    s=s+z
    print('s=', s)
    i=i+1
    print('i=', i)
    print('\n')
print(s)

#ex24
from turtle import *
color('purple')
speed(10)
pos()
i=0
while True :
    i=i+1
    print(i)
    forward(70)
    left(90)
    if abs(pos())<1:
        break
done()

#ex25
from turtle import *
for i in range(5):
    forward(100)
    left(90)
mainloop()

from turtle import *
rayon=20
while rayon<100 :
    circle(rayon)
    up()
    right(90)
    forward(10)
    left(90)
    down()
    rayon=rayon +10
mainloop()

#ex26 question1
n=int(input('Entrez le nombre de côtés du polygone régulier à tracer: \n')
up()
goto(0,100)
down()
for i in range (n):
      forward(50)
      left(360/n)
mainloop()


#question2
from turtle import*
l=300
while l<5:
    for i in range (2):
        forward(l)
        left(90)
        l=l-5
mainloop()

def f(x):
    return x**3-3*x+5


#ex28
def valAbs(x):
    if x>=0:
        res=x
    else :
        res=-x
    retur��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������