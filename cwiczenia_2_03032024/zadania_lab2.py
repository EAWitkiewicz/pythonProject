import sys
import math
#Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz
# po dwie zmienne każdego typu a następnie wyświetl
#te zmienne
a=6
b=9
c=2.1
d=3.7
e="Pogrzeb kota"
f="""I nawet kiedy
bede saaaaaam
nie zmienie sie
to nie moj swiat"""
g=complex(111,222)
h=complex(333,444)
print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",)

#ad2. Stwórz skrypt kalkulator,
#w którym wykorzystać wszystkie podstawowe działania arytmetyczne

"""liczba_1=input("Podaj liczbe: \n")
operacja=input("Podaj operacje: \n")
liczba_2=input("Podaj druga liczbe \n")
def kalkulator(liczba_1,operacja,liczba_2):
    if operacja=="+":
        print(int(liczba_1)+int(liczba_2))
    if operacja=="-":
        print(int(liczba_1)-int(liczba_2))
    if operacja==":":
        print(int(liczba_1)/int(liczba_2))
    if operacja=="*":
        print(int(liczba_1)*int(liczba_2))

kalkulator(liczba_1,operacja,liczba_2)
"""
#Zad3. Napisz skrypt, w którym
# stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
euler=math.exp(10)
print(euler)
dzialanie2=math.pow(math.log(5 + math.sin(8)**2), 1/6)
print(dzialanie2)
dzialanie3=math.floor(3.55)
print(dzialanie3)
dzialanie4=math.ceil(4.8)
print(dzialanie4)

#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej
#metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody
#capitalize)
imie="ELA"
nazwisko="WITKIEWICZ"

print(imie.capitalize(),nazwisko.capitalize())

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się
#słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba
#użyć metody count)