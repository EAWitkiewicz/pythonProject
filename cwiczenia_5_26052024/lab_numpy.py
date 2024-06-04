import numpy as np

# #WEKTORY---------------------
# a=np.array([20,30,40,50])
# print(a)#w:[20,30,40,50]
# b=np.arange(4)#w:[0 1 2 3]
# print(b)
#--------odkomentowac fragment poniezj do przykladow do koeljnej lini z myslnikow
##DZIALANIA NA WEKTORACCH
# c=a-b#[20-0,30-1,40-2,50-3]
# print(c)#w:[20 29 38 47]

# print(b**2)#[0**2 1**2 2**2 3**2]
# #w:[0 1 4 9]

# a+=b#[20+0 30+1 40+2 50+3]
# print(a)#w:[20 31 42 53]
# a-=b#[20-0 31-1 42-2 53-3]
# print(a)#[20 30 40 50]

# #MNOZENIE WEKTORÓW
# d=a*b
# print("\n",d,"\n")#[20*0 30*1 40*2 50*3]
# #w:[  0  30  80 150]
# # Tworzenie tablicy numpy z jednym elementem o wartości 3
# b=np.array(3)
# print(b)# Wydrukowanie tablicy 'b': 3
# print(np.exp(b))# Wydrukowanie wyniku funkcji wykładniczej dla tablicy 'b': 20.085536923187668
# print(np.sqrt(b))# Wydrukowanie wyniku pierwiastkowania dla tablicy 'b': 1.7320508075688772
# c=np.array([2.,-1,4.]) #rzykladowy wektor z elementó:[ 2. -1.  4.]
# print(c)
# print(np.add(b,c))#[ 2.+3 -1.+3  4.+3]
# #w:[5. 2. 7.]
#------------------------------------------------------------------------
#MNOZENIE MACIERZY#######################################################
# a=np.arange(3) # Tworzenie tablicy numpy z wartościami [0, 1, 2]
# b=np.arange(3) # Tworzenie tablicy numpy z wartościami [0, 1, 2]
# print(a) #W:[0 1 2]
# print(b)#W:[0 1 2]
# # Obliczenie iloczynu skalarnego (dot product)
# # tablic 'a' i 'b', a następnie wydrukowanie wyniku
# print(a.dot(b))# Iloczyn skalarny: 0*0 + 1*1 + 2*2 = 0 + 1 + 4 = 5
# # Wynik: 5
# # Obliczenie iloczynu skalarnego (dot product)
# # tablic 'a' i 'b', a następnie wydrukowanie wyniku
# print(np.dot(a,b))# Iloczyn skalarny: 0*0 + 1*1 + 2*2 = 0 + 1 + 4 = 5
# # Wynik: 5
# c=np.array([[1,5],[2,6],[7,4]])
# d=np.array([[2,5,4],[4,3,1]])
#
# print("Macierz c:\n", c, "\n")
# print("Macierz d:\n",d, "\n")
# print("Wynik mnozenia macierzy c * d: ", np.dot(c,d), "\n")
# # [[ 22 20  9]   # (1*2 + 5*4) (1*5 + 5*3) (1*4 + 5*1)
# #  [ 28 28 14]   # (2*2 + 6*4) (2*5 + 6*3) (2*4 + 6*1)
# #  [ 30 47 36]]  # (7*2 + 4*4) (7*5 + 4*3) (7*4 + 4*1)
# print(np.dot(d,c))

# #SUMA ELEMENTÓW MACIERZY
# # Tworzenie tablicy numpy z wartościami od 0 do 11,
# # a następnie przekształcenie jej w macierz 3x4
# a=np.arange(12).reshape((3,4))
# print(a)
# # Wynik:
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
# print(a.sum())# Obliczenie sumy wszystkich elementów w macierzy 'a' i wydrukowanie wyniku
# # Wynik: 66
# print(a.sum(axis=0))# Obliczenie sumy elementów wzdłuż osi 0 (dla każdej kolumny) i wydrukowanie wyników
# # Wynik: [12 15 18 21]
# # (0+4+8, 1+5+9, 2+6+10, 3+7+11)
# # Obliczenie minimalnej wartości wzdłuż osi 1 (dla każdego wiersza)
# # i wydrukowanie wyników
# print(a.min(axis=1))
# # Wynik: [0 4 8]
# # (min(0,1,2,3), min(4,5,6,7), min(8,9,10,11))
# print(a.cumsum(axis=1)) #axis 1-wiersze axis-0 kolumny
# # Wynik:
# # [[ 0  1  3  6] 1)
# #  [ 4  9 15 22]
# #  [ 8 17 27 38]]
# #1)Pierwszy wiersz [0, 1, 2, 3]:
# # Skumulowana suma zaczyna się od pierwszego elementu: 0
# # Dodajemy drugi element: 0 + 1 = 1
# # Dodajemy trzeci element: 1 + 2 = 3
# # Dodajemy czwarty element: 3 + 3 = 6
# # Wynik dla pierwszego wiersza: [0, 1, 3, 6]

# #PETLE NA MACIERZACH
# a=np.arange(6).reshape((3,2))
# #print(a)
# #w:[[0 1]
#  # [2 3]
#  # [4 5]]
#
# for b in a: #element b, bedzie jako pojedynczy wiersz
#     print(b)
#     # w:[0 1] bez nawiasu na zewnatrz
#     # [2 3]
#     # [4 5]
#
# for b in a.flat:#.flat splaszcza macierz do wektora
#     print(b)
# #w:0
# # 1
# # 2
# # 3
# # 4
# # 5
#
# for b in a:  # Iteracja po każdym wierszu macierzy 'a'. 'b' będzie pojedynczym wierszem macierzy 'a'
#     for i in range(len(b)):  # Iteracja po każdym elemencie wiersza 'b'
#         print(b[i], end=' ')  # Wydrukowanie każdego elementu wiersza z odstępem
#         print()  # Przejście do nowej linii po wydrukowaniu elementu
#         #w:0
#         # 1
#         # 2
#         # 3
#         # 4
#         # 5
# # Tworzymy dwuwymiarową tablicę o wymiarach 3x2
# a=np.arange(6).reshape((3,2))
# print(a)
# print(a.shape)# Wyświetlamy kształt tablicy (ilość wierszy i kolumn) w:(3, 2)
# print(type(a))#w:<class 'numpy.ndarray'>
# # Pętla iterująca po wierszach tablicy
# for i in range(0,a.shape[0]):#a.shape[0] odwolanie sie do wierszy czyli tu = 3
#     # Pętla iterująca po kolumnach tablicy
#     for j in range(0,a.shape[1]):#a.shape[1] odwolanie sie do kolumn czyli tu = 2
#         # Wyświetlamy element tablicy o indeksach [i, j]
#         print(a[i][j],end=' ')
#     print(" ")

# #PRZEKSZTALCANIE MACIERZY
# a=np.arange(6)
# print(a)#w:[0 1 2 3 4 5]
# print(a.shape)#w:(6,)
# print("")
# b=a.reshape((2,3))#uwtorzenie z wektora macierzy 2x3
# print(b)
# #wynik:
# #[[0 1 2]
# # [3 4 5]]
# print(b.shape)#w:(2, 3)
# print("")
# c=b.reshape((3,2)) #przeksztalcanie macierzy 2x3 na macierz 3x2
# print(c)
# #wynik:
# # [[0 1]
# #  [2 3]
# #  [4 5]]
# print(c.shape)#w:(3, 2)
# print("")
# #Metoda ravel odtwarza wektor wejsciowy, splaszcza macierz do rozmiarow 1 na x elementow
# d=c.ravel()
# print(d)#w:[0 1 2 3 4 5]
# print(d.shape)#(6,)
# print("")
# #TRANSPOZYCJA MACIERZY
# e=b.T
# print(e)
# #wynik: działa inaczej niz reshape ,reshape wbija eleemnty
# #a transpozycja wpisuje wiersze jako kolumny
# #[[0 3]
#  # [1 4]
#  # [2 5]]
# print(e.shape)


# CO DO NUMPY TO TYLE
# import pandas as pd
#
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s)
# data = {'Kraj': ['Belhia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brazylia'],
#         'Populacja': [11190846, 13031171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)
#
# print(s['c'])
# print(s.c)
# print(df[0:1])
# print("")
# print(df['Populacja'])
# print(df.iloc[0.0])
# print(df.loc[0, "Kraj"])
# print(df.a[0, "Kraj"])
# print('kraj' + df.Kraj)
# print(df.sample())
