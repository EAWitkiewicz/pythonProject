import sys
import random
# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
print("zadanie 1")
#A od 0 do -9
A=[1-x for x in range(1,11)] #TODO minusowe
print(A)
#B 4 do potego 7
B=[4**i for i in range(8)]
prnt(B)
# #C to co w b podzielne przez 2
# C=[x for x in B if x%2==0]
# print(C)

#Zad 2
#Wygenereuj losowo 10 elementow
#zapisz je do listy1
# a nastepnie wykorzystujac python comprehesion
# zdefiniuj nowa lie ktora bedzie zawierala
# tylko parzyste elementy
# lista=[x for x in range(10)]
# print(lista)

# randomlist = []
# for i in range(0,5):
#     n = random.randint(1,10)
#     randomlist.append(n)
# print(randomlist)

losowe = [random.randint(1,100) for x in range(10)]
print(losowe)