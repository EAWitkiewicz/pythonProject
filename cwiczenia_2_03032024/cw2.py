import sys

# ctrl + / komentowanie wiekszej ilosci kodu
# a=56
# print(a)
# print(type(a)) #sprawdza typ
# b=5.5
# print(b)
# zmienna_tesktowa='napis'
# print(zmienna_tesktowa)
# print(type(zmienna_tesktowa))

# a = 6
# b = 3

# c = a + b
# print(c)

# d = a - b
# print(d)

# e = 4
# f = b // a
# print(f)
# f = a // b  # dzielnie calkowite
# print(f)

# g = a ** 2  # potegowanie (szczegolnie ok jak nie ma ulamkow)
# print(g)
# h = pow(a, 2)  # tez potegowanie
# print(h)

# tu nie bedzie taki sam wynik bo kolejnosc dzialan
# i = 6 ** 1 / 2
# j = pow(6, 1 / 2)
# za to jak dasz w nawias to juz bedzie :)
# i2 = 6 ** (1 / 2)
# print(i)
# print(j)
# print(i2)

#   TUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
# k = 'wizualizacja danych'
# l = 'grupa'
# m = 2
# print(k+l+str(m))
# print('liczba a jest rowna {:d} liczba b jest rowna {:d}'.format(a,b))
# format liczb dziesietnych {:d}
#
#
#
# a = input('sprawdz liczbe: ')
# print(a)
# print(type(a))
# a = int(a)
# print(a*5)
# print(type(a))
#
# sys.stdout.write('Wprowadz liczbe ')
# b = sys.stdin.readline()
# # readline dodaje na koncu znak nowego wiersza automatycznie
# print(b + ' to wartosc liczby b')
# print(type(b))
#
#
#
#lista = [5, 6.6, 36, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# # dodanie nowego elementu na koncu listy
# lista.append(67)
# print(lista)
# # 1 pozycja: na ktora pozcyje ma wskoczyc(numeracja od zera) w przypadku
# 2 bedzie miedzy 1 a 2 indeksem ,2 pozycja: co ma byc wepchnete w liste
# lista.insert(2, 'c')
# print(lista)
# # kilk aelementow na koniec listy,musza byc lista al enie zostana dodane jako lista tylko ajko oddzialne elementyS
# lista.extend([20, 21, 22])
# print(lista)
# # usunie ostatni element z listy
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# # usuwaa elementy po wartosci
# lista.remove([2, 3, 4])
# print(lista)
# # uwunie calkowiccie lista jak nie poda sie wartosci zostanie usunieta z pamieci
# del lista[1]
# print(lista)
# # odwaraca calkowicie liste
# lista.reverse()
# print(lista)
# # lista sort sortujr elementy ale musza byc te same wartosci/typy bo jak sa napisy z intami to sie wywali
# lista.sort()
# print(lista)
#
#
#
# slownik = {'klucz': 'wartosc', 1: 2, 'a': 5, 4: 'b'}
# # klucze sa unikatowe
# print(slownik)
# print(slownik[4])
# # dodawnie elemntow do slownika
# slownik[6] = 45
# print(slownik)
# # usuwanie,tylko koniecznie trzeba podac argumrnt, podaje sie klucz i element po tym kluczu
# # 1: 2
# # 1-to klucz, 2-wartosc
# slownik.pop(1)
# print(slownik)
# slownik(slownik.keys())
# slownik(slownik.values())
# del slownik[6]
# # jak beda dwa takie same klucze to sie nadpiszą i bedzie ten ostatni
# #
# #
# #
# #
# ############INSTRUKCJE WARUNKOWE ##########################################################################
# a = 6
# b = 7
# if a > b:
#     print("a wieksze od b")
# elif a < b:
#     print("a mniejsze b")
# else:
#     print("a jest rowne b")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)

# petle
# for i in range(8):
#     print(i)
# else:
#     print('koniec petli')

# petla od 2 do 7
# for i in range(2, 7):
#     print(i)
# else:
#     print('koniec petli')

# petla od 2 do 8 co 2 kroki
#
# (odkomentuj liste)
# for i in lista:
#     print(i)
# petla zagniezdzona
# for i in range(0, 5):
#     for j in range(0, 5):
#         result = i+j
#         print(result)
#     print('')

# # while i przechodzenie po waszytskich elementach listy
# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('koniec petli')
#
# licznik = 0
# while licznik!= 10:
#     if licznik == 7:
#         print(licznik)
#         break
#     else:
#         licznik +=1
# else:
#     print('licznik')

# ZADANIE
i = 0
lista = [1, 2, 3, 4, 5, 6]
liczba_wczytana = int(input())

while i < len(lista):
    if liczba_wczytana - lista[i] == 0:
        break
    i += 1
else:
    print('liczba podana nie jest z listy')
