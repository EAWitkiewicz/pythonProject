import sys
import random
import math
# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
print("zadanie 1")
#A od 0 do -9
A=[1-x for x in range(1,11)]
print(A)
#B 4 do potego 7
B=[4**i for i in range(8)]
print(B)
# #C to co w b podzielne przez 2
C=[x for x in B if x%2==0]
print(C)
print("\n")
#Zad 2
#Wygenereuj losowo 10 elementow
#zapisz je do listy1
# a nastepnie wykorzystujac python comprehesion
# zdefiniuj nowa lie ktora bedzie zawierala
# tylko parzyste elementy
print("zadanie 2")
losowe = [random.randint(1,100) for x in range(10)]
print(losowe)
losowe_parzytse=[x for x in losowe if x%2==0]
print(losowe_parzytse)
print("\n")
#Zad 3
#utworz slownik z produktami spozywczymi do kupienia gdzie:
#klucz to bedzie nazwa produktu a wartosc to jednostki np kg ,sztuki itd itp
#wykorzystaj pythoon comprehesion do zdefiniowania
#nowej listy gdzie produkty ktorych wartosci to sztuki
print("zadanie 3")
jedzonko={"ser":"gr","jablka":"sztuki","szynka":"plasterki","awokado":"sztuki","wodka":"litry","kawa":"litry","gruszki":"sztuki"}
print(jedzonko)
jedzonko_na_sztuki=[wartosc for wartosc,jednostka in jedzonko.items() if jednostka=='sztuki']
print(jedzonko_na_sztuki)
print("\n")

#Zad 4
#zdefiniuj funcje ktora sprawdzi czy trojkat jest prostokatny
print("zadanie 4")
def trzojkat(a,b,c):
    if a**2 +b**2 ==c**2:
        print("prostkatny")
        return True
    else:
        print("nie prostokatny")
        return False
print("boki 3,4,4:")
trzojkat(3,4,4)
print("boki 3,4,5:")
trzojkat(3,4,5)
print("\n")
#Zad 5
#Zdefiniuj funkcje ktora policzy pole trapezu.
#fukcja ma przyjmowac wartosci domyslne
print("zadanie 5")
def poletrapezu(a=6,b=10,h=8):
    return ((a+b)*h)*(1/2);
print(poletrapezu());
print("\n")
#Zad 6
#Zdefiniuj fukcje ktora bedzie liczyc iloczyn elementow ciagu
#parametr funcji a1 wartosc poczatkowa
#b- wielkosc o ile mnozone sa kolejne elementy
#ile ile elementow ma mnozyc
#ma przyjmowac wartosci domyslne a=1,b=4,ile=10
print("zadanie 6")
def jakis_ciag(a=1,b=4,ile=10):
    iloczyn=1;
    for a in range(a,ile+1):
        iloczyn=iloczyn+a*b
        print("iloczyn",iloczyn)
        print("a",a)
    return iloczyn

jakis_ciag()
print("\n")
#zad 7
#Napisz skrypt ktory liczy pierwiastek z liczby podnej przez uzytkownika
#jesli uzytkownik poda wartosc ujemna to powinien byc wylapany blad
print("zadanie 7")
liczba_uzytkownika=input("podaj liczbe do pierwiastka\n")
try:
    liczba_uzytkownika=float(liczba_uzytkownika)
    if liczba_uzytkownika>=0:
        pierwiastek=math.sqrt(liczba_uzytkownika)
        print(pierwiastek)
    else:
        raise ValueError("liczba uzytkownika")
except ValueError:
    print("z ujemnej nie da rady")