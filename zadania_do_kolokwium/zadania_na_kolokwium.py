import sys
import math as m
import random as r

# #zad 1 liczenie i wyswietlanie wyrazen
# print("Zadanie 1")
# dzialnie1=(m.exp(4)-m.log2(34))**(1/3)
# print(dzialnie1)
# dzialnie2=(m.cos(45)+m.exp(1)+m.log1p(20))**(1/3)
# print(dzialnie2)
# dzialnie3=(m.log(20,3)+m.sin(45)*(5/8))**(1/4)
# print(dzialnie3)
# dzialnie4=m.log(23,3)+(m.sin(34)+5)**(1/3)
# print(dzialnie4)
# dzialnie5=((m.log2(32)+m.pi+m.sin(56)))**(1/4)
# print(dzialnie5)

# print("\nZadnie 2")
# podana=input("Podaj wysokosc wierzy miedzy 0 a 10: ")
# if(int(podana)<=10):
#     for i in range(int(podana)+1):
#         for j in range(i):
#                 print("A",end='')
#         print()
# else:print("WIEKSZA OD 10!!!")

# print("\nZadnie 3")
# podana1=input("Podaj wysokosc wierzy miedzy 0 a 10: ")
# if(int(podana1)<=10):
#     for i in range(0,int(podana1)):
#         for k in range(int(podana1)-i-1):
#             print("_",end='')
#         for j in range(i*2+1):
#             print("A",end='')
#         print()
# else:print("WIEKSZA OD 10!!!")

print("\nZadnie 4")
wektor=r.randint(2,10)
k=wektor
r=wektor
macierz=[[r.random() for _ in range(k)] for _ in range(r)]
print(macierz)
#help(random)


