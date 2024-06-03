
import numpy as np

# # Zadania
# # Zad1.
# # Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15
# #kolejnych wielokrotności liczby 3.
# #numpy.arange([start, ]stop, [step, ]dtype=None)
# tablica = np.arange(3, 3 * 15 + 1, 3)
# print(tablica)

# # Zad2.
# # Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do
# # innej zmiennej jej
# # kopię przekonwertowaną na typ int64
# #generuje 10 elementow!
# tab = np.arange(0, 5, 0.5, dtype='float64')
# #wynik:[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
# #czyli:[0.0  0.5  1.0  1.5  2.0  2.5  3.0  3.5  4.0  4.5]
# #       1     2    3    4   5    6     7    8   9     10
# # Tworzy nową tablicę (tab1) na podstawie tablicy tab,
# # ale przekształca typ danych elementów na int64, czyli całkowite 64-bitowe.
#
# # Wszystkie wartości po przekształceniu będą zaokrąglane
# # w dół do najbliższej liczby całkowitej.
# tab1 = tab.astype("int64")
# #wynik: [0 0 1 1 2 2 3 3 4 4]
# print(tab)
# print(tab1)

# # Zad3.
# # Napisz funkcję, która będzie:
# # • Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# # • Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
# n1 = int(input("Podaj liczbe :"))#np. 5
# def zwroci_tablice(n1):
#
#     elementy = np.arange(n1*n1) #genruje 5*5=25 elementow
#     tablica = np.reshape(elementy,(n1,n1)) #wpiernicza je w macierz 5x5
#     return tablica
#
# print(zwroci_tablice(n1))

# #Zad4.
# #Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# #potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj
# #tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
# def zad4(podstawa, potegi):
#     lista = np.logspace(1, potegi, num=potegi, base=podstawa)
#     #startuje od potego 1 jest tyle elementow co poteg
#     # Używa np.logspace do generowania sekwencji logarytmicznej zaczynającej
#     # się od podstawa ^ 1 do podstawa ^ poteg(potegi) go potega(elemntow)
#                 #2**1   2**2    2**3    2**4
#     return lista
# print(zad4(2,4))

# # Zad5.
# # Napisz funkcję, która:
# # • Na wejściu przyjmuje jeden parametr określający długość wektora
# # • Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# # • Generuj macierz diagonalną z w/w wektorem jako przekątną
# def mdiag_z_wektorem_po_przekotnej(dl_wektora):
#     # Tworzenie wektora o długości dl_wektora, zawierającego liczby od dl_wektora
#     # do 1 włącznie, z krokiem -1
#     wektor=np.arange(dl_wektora,0,-1)
#     # Tworzenie macierzy diagonalnej na podstawie utworzonego wektora
#     macierz_diagonalna=np.diag(wektor)
#     return macierz_diagonalna
# print(mdiag_z_wektorem_po_przekotnej(5))

# # Zad6.
# # Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci
# # wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# # Jedno z tych słów powinno być wypisane od prawej do lewej.
# slowo1='wszytsko jedno'
# slowo2='marsz marsz'
# slowo3='trojkat'
#
# #znajduje najdluzsze slowo na podstawie ktorego bedzie tworzona macierz
# rozmiar=max(len(slowo1),len(slowo2),len(slowo3))
# #tworzy macierz o rozmiarze maksymalnego slowa ,wypelniona zereami domyslnie,z typem danych unicode
# macierz=np.full((rozmiar,rozmiar),0,dtype='<U1')
# #wypisaywanie od tylu
# #[poczatkwoy element:koncowy element:krok] wycinanie w pythonie
# odwroconeslowo=list(slowo2)[::-1]
# #poziomo
# #wstaawianie slowa od 0 wiersza do liczby kolumn+1
# # o punktu macierz[wiersz,kolumna]=wstawiomy slowo
# macierz[0, 1:1+len(slowo2)] =odwroconeslowo
# #pionowo
# # o punktu macierz[wiersz,kolumna]=wstawiomy slowo
# macierz[1:len(slowo3)+1,0]=list(slowo3)
# #po ukosie
# #wstawia n.fill_diagonal(gdzie?,co?)
# np.fill_diagonal(macierz,list(slowo1))
#
# print(macierz)

# Zad7.
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
# [4 2 4]
# [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność
# liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
def generacja_macierzy(n):
    macierz=np.zeros((n,n))
    wektor=np.full(n,2)
    przekatna=0
    while(przekatna <n):
        #np.fill_diagonal(macierz[przekatna:],wektor,przekatna)
        przekatna=przekatna+1
        wektor=wektor+2

    return macierz
print(generacja_macierzy(4))

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
