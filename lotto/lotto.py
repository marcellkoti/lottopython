#Lottósorsolás 
#kérjük meg a felhasználót hogy válasszon milyen lottót szeretne játszani
#: 5,6,skandináv
#5: 5számot kell eltalálni a 90-ből 5/90
#6: 6/45
#skandináv: 7/35 --> 2 X húzzák ki a hetet (14)
import random
otos = []
for i in range(0,90):
    print(i+1,sep='\t',end=',')


hatos = []

for i in range(0,46):
    print(i,sep='\t',end=',')
    

skandinav = []

for i in range(35):
    skandinav.append(random.randint(0,36))


print()

lotto = input("Válasszon milyen lottót szeretne játszani (5-ös, 6-os, Skandináv)? ")
while lotto != "5" and lotto != "6" and lotto != "skandináv" :
    lotto = input("Válasszon milyen lottót szeretne játszani (5-ös, 6-os, Skandináv)? ")
    ot = 0
    

   























