import sys as system
import re

# Zad 1. Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input
# print("zadanie 1")
# zdanie=input("Podaj zdanie aby policzyc ile ma slow\n")
# #mozna to bylby bo zrobic splitem albo liczyc spacje countem ale zrobimy inaczej
# #bo z uzytkownikiem to nigdy nie wiadomo
# slowa = re.findall(r'\b\w+\b', zdanie)
# #lub
# #slowa=zdanie.split()
# #\b onzacza granice slowa \w+ dowolny znak litere/cyfre/podkreslenie r' sprawia ze backslache sa ignorowane
# #nie sa znakami specjalnymi
# liczba_slowa=len(slowa)
# print("liczba slowa: {}\n".format(liczba_slowa))




# Zad 2. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz
# obliczenia: ab + c.
# Użyj funkcji readline() i write()).
#print("zadanie 2")#
# #nadal niepewnie mi sie tego uzywa
# print("Writline i readline podaj a b i c:\n")
# a=system.stdin.readline()
# b=system.stdin.readline()
# c=system.stdin.readline()
# obliczenie=int(a)**int(b)+int(c)
# system.stdout.write("a**b+c="+str(obliczenie)+"\n")



# # Zad3. Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem.
# print("zadanie 3")
zdanie1 =input("Podaj zdanie aby sprawdzic czy jest palindromem: ")
zdanie_bez_spacji_i_wszytskie_male_litery=zdanie1.replace(" ","").lower()
zdanie_zlisowane=list(zdanie_bez_spacji_i_wszytskie_male_litery)
zdanie2=zdanie_zlisowane
zdanie_zlisowane.reverse()
if zdanie_zlisowane==zdanie2:
    print("spalindromowane")
else:
    print("nie spalindromowane")


# if zdanie1.remove(" ")==list((zdanie1.reverse())).remove(" "):
#     print("Palindromowane")
# else:
#     print("nie palindromowane")


# # Zad4. Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza.
# print("zadanie 4")
# liczba=int(input("Podaj liczba zby sprawdzic czy  jest pierwsza"))
# licznik=0
# for i in range(1,liczba+1):
#     if liczba%i==0:
#         licznik=licznik+1
# if licznik>2:
#     print("liczba nie jest pierwsza")
# else:
#     print("liczba jest pierwsza")



# Zad5. Napisz skrypt, który sprawdzi ile jest liczb doskonałych do liczby 1000.
# print("zadanie 5")
# ile_doskonalych=0
# for i in range(1,1001):
#     suma_dzielnikow = 0
#     for j in range(1,i):
#         if i%j==0:
#             suma_dzielnikow=suma_dzielnikow+j
#     if suma_dzielnikow==i:
#         ile_doskonalych=ile_doskonalych+1
#         print("doskonała liczba nr %d: %d" %(ile_doskonalych,i))
# print("Wszytskich liczb doskonalych w zakresie od 1 do 1000 jest: ",ile_doskonalych)



# # Zad 6. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i
# # float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
# print("zadanie 6")
# print("Elementy listy do kwadratu: ")
# lista=[1,2.2,3,4.4,5,6.6,7]
# print(lista)
# for i in range(0,len(lista)):
#     print((lista[i])**2)

# # Zad 7. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# # następnie dodaje do listy tylko parzyste liczby.
# print("zadanie 7")
# i=0
# lista1=[]
# while i!=10:
#     i=i+1
#     liczba_pobrana=input("Podaj liczbe ktora ma byc dodana do listy: ")
#     if (float(liczba_pobrana)%2==0):
#         lista1.append(liczba_pobrana)
#
# print(lista1)


# Zad 8.
# Napisz skrypt, w którym utworzysz listę z elementami dowolnego
# typu.
# Utwórz słownik, gdzie klucze będą poszczególnymi elementami z listy,
# a wartość to ilość wystąpień klucza w liście.
# Następnie usuń wszystkie elementy ze słownika, które nie będą liczbami.
lista2=("element","dowolnego typu",777,99.9,'x',6,6,6,"slowo")
slownik={}

#petla ktora dodaje jak leci klucze w slowniku cos w styli slownik[i]=lista[i]
#petla albo count ktora zlicza wystapienia tych kluczy
#petla ktora wpisuje wystapienia do tych kluczy
#petla usuwajaca po kluczach
for i in lista2:
    for j in slownik:
        slownik[j]=i

print(slownik)





