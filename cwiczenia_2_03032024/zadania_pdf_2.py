import sys as system
import math

#Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
sporty=["euknkanto","boks szachowy","flanki","podwodny hokej","wyscig strusi","cheese-rolling"]
print(sporty)
sporty.reverse()
print(sporty)
sporty.extend(["kutarate","Quidditch"])
print(sporty)
#chodzi ododanie odtakowego sportu czy o zmiane kolejnosci?



#Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub
# artykułach internetowych. Jako klucz przyjmij skrót danego słowa,
# wartość to rozwinięcie tego skrótu.

#nie beda z gazet
print("zadanie 2 z deklaracja slownika")
slownik={'kc':"kohcham cie",'pzdr':"pozdro",'cb':"Ciebie",'w8':"wait"}
print(slownik)


#Zad 3. Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
print("zadanie 3")
gierki={1:"untitled goos game",2:"Counter-Strike",3:"Mario"}
ilosc_kluczy=len(gierki)
print(gierki)
print("tyle jest elementow a w zasadzie kluczy :",ilosc_kluczy)



#Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy
# wystąpienia litery a. Użyj funkcji input
print("zadanie 4")
zdanie=input("Podaj zadanie z literkami do zliczenia literek a:\n")
ile_a=zdanie.count("a")
print(ile_a)


#Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie
# wykonasz obliczenia: ab + c. Użyj instrukcji readline() i write()).
print("zadanie 5")
print("Writline i readline podaj a b i c:\n")
a=system.stdin.readline()
b=system.stdin.readline()
c=system.stdin.readline()
obliczenie=int(a)*int(b)+int(c)
system.stdout.write("a*b+c="+str(obliczenie)+"\n")


#Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich
# jest największa. W zależności od wyniku wyświetl odpowiedni komunikat.
# Użyj zagnieżdżeń.
print("zadanie 6:")
print("Maximum: ")
a1=int(input("Podaj a: "))
b1=int(input("Podaj b: "))
c1=int(input("Podaj c: "))
def maximum (a,b):
    if a>b:
        return a
    else:
        return b

print(maximum((maximum(a1,b1)),c1))


#Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb
# typu int i float. Następnie za pomocą użycia pętli for podnieś
# każdą liczbę do kwadratu.
print("zadanie 7")
print("Elementy listy do kwadratu: ")
lista=[1,2.2,3,4.4,5,6.6,7]
print(lista)
for i in range(0,len(lista)):
    print((lista[i])**2)



#Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.
print("zadanie 8")
i=0
lista1=[]
while i!=10:
    i=i+1
    liczba_pobrana=input("Podaj liczbe ktora ma byc dodana do listy: ")
    if (float(liczba_pobrana)%2==0):
        lista1.append(liczba_pobrana)

print(lista1)


#Zad. 9.
#Napisz skrypt, który liczy pierwiastek z liczby podanej przez
# użytkownika jeśli użytkownik poda wartość ujemną to powinien
# być wyłapany błąd.
liczba_do_pierwiastka=input("Podaj co tam chcesz pierwiastkowac: ")

try:
    wynik=math.sqrt(int(liczba_do_pierwiastka))
    print(wynik)
except ValueError as error:
    print("Ziomus ale nie ujemna...\n masz nawet nazw tego bledu:\n",error)