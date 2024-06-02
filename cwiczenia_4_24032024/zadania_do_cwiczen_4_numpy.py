import numpy as n

# # Zadania
# # Zad1.
# # Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.
# tablica = n.arange(3, 3 * 15 + 1, 3)
# print(tablica)
#
# # Zad2.
# # Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do
# # innej zmiennej jej
# # kopię przekonwertowaną na typ int64
# tab = n.arange(0, 5, 0.5, dtype='float64')
# tab1 = tab.astype("int64")
# print(tab)
# print(tab1)
#
# # Zad3.
# # Napisz funkcję, która będzie:
# # • Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# # • Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
# n1 = int(input("Podaj liczbe :"))
#
#
# def zwroci_tablice(n1):
#     tab2 = n.array([n.arange(n1), n.arange(n1)])
#     return tab2
#
#
# print(zwroci_tablice(n1))
#
#
# # Zad4.
# # Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# # potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj
# # tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
# def zad4(podstawa, ile_poteg):
#     lista = n.logspace(1, ile_poteg, num=ile_poteg, base=podstawa)
#     #startuje od potego 1 jest tyle elementow co ile_poteg
#     # Używa np.logspace do generowania sekwencji logarytmicznej zaczynającej
#     # się od podstawa ^ 1 do podstawa ^ ile_poteg z ile_poteg
#     # próbkami.
#     return lista
# # print(zad4(2,4))
# # Zad5.
# # Napisz funkcję, która:
# # • Na wejściu przyjmuje jeden parametr określający długość wektora
# # • Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# # • Generuj macierz diagonalną z w/w wektorem jako przekątną
# def mdiag_z_wektorem_po_przekotnej(dl_wektora):
#     wektor=n.arange(dl_wektora,0,-1)
#     macierz_diagonalna=n.diag(wektor)
#     return macierz_diagonalna
# print(mdiag_z_wektorem_po_przekotnej(5))

# Zad6.
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci
# wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.
slowo1='wszytsko jedno'
slowo2='marsz marsz'
slowo3='trojkat'

#znajduje najdluzsze slowo na podstawie ktorego bedzie tworzona macierz
rozmiar=max(len(slowo1),len(slowo2),len(slowo3))
#tworzy macierz o rozmiarze maksymalnego slowa
macierz=n.full((rozmiar,rozmiar),0,dtype='<U1')
#poziomo
#wstaawianie slowa od 0 wiersza do 1:kolumny
#wypisaywanie od tylu
#[poczatkwoy element:koncowy element:krok] wycinanie w pythonie
odwroconeslowo=list(slowo2)[::-1]
macierz[0, 1:1+len(slowo2)] =odwroconeslowo
#pionowo
macierz[1:len(slowo3)+1,0]=list(slowo3)
#po ukosie
n.fill_diagonal(macierz,list(slowo1))

print(macierz)
# Zad7.
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
# [4 2 4]
# [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność
# liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

# Zadanie 8
# Napisz funkcję, która:
# • jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr
# ‘kierunek’,
# • parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# • funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość
# wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)

# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie
# zawierała kolejne wartości ciągu Fibonacciego.
