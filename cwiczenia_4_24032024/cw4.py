import sys
import numpy as np
# # Utworzenie jednowymiarowej tablicy numpy z elementami 0 i 1
# a = np.array([0, 1])
# print(a)
# #wynik: [0 1]
#
# # Utworzenie jednowymiarowej tablicy numpy z elementami od 0 do 1
# a = np.arange(2)  # petla od i=0 do i=2
# print(a) #wynik: [0 1]
# print(type(a)) #wynik: <class 'numpy.ndarray'>
# # typ elementow jakie tablica przchowuje
# print(a.dtype)  #wynik: int32

# #to samo co wyzej ale z okreslonym typem danych
# a = np.arange(2, dtype='int32')
# print(a.dtype) #wynik: int32
# # Konwersja typu danych tablicy 'a' na float i zapisanie wyniku do nowej tablicy 'b'
# b = a.astype('float')  # w kopi inty sa zamieniane na foaty
# print(b) #wynik:[0. 1.]
# print(b.dtype) #wynik: float64
# print(b.shape) # Wyświetlenie kształtu tablicy 'b' wynik:(2,) czyli
# #W tym przypadku (2,) oznacza, że tablica b jest wektorem (jednowymiarową tablicą) o długości 2.
# print(a.ndim)  # ile wymiarowa tablica wynik:1

# # tworzenie tablicy dwowymiaorwej z dwoma elementami w każdym wierszu
# m = np.array((np.arange(2), np.arange(2)))
# print(m)
# # Wynik:
# # [[0 1]
# #  [0 1]]
# print(m.shape) #wynik: (2,2)
# print(m.ndim) #wynik: 2
#
# m2 = np.array([[2, 3, 5], [2, 4, 6]])
# print(m2)#[[2 3 5][2 4 6]]
# print(m2.shape) #wynik :(2, 3)
# wektor = np.arange(5) # Tworzenie jednowymiarowego wektora z wartościami od 0 do 4
# print(wektor)#w:[0 1 2 3 4]

# # Tworzenie dwuwymiarowej tablicy 5x5 wypełnionej zerami
# zera = np.zeros((5, 5))
# # Tworzenie dwuwymiarowej tablicy 4x4 wypełnionej jedynkami
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)#w: float64
# print(jedynki.dtype)#w: float64

# # Tworzenie dwuwymiarowej tablicy 2x2 z niezainicjalizowanymi wartościami
# # (wartości będą losowe, zależne od pamięci)
# pusta = np.empty((2, 2))
# print(pusta)
# # Wynik (przykładowy, wartości mogą być różne):
# # [[ 6.95562623e-169 -2.61834153e+077]
# #  [-7.85235246e+111  4.36157412e-072]]
# poz_1 = pusta[1, 1]  # index wiersza index kolumny
# poz_2 = pusta[0, 1] # Pobranie wartości z tablicy 'pusta' z pozycji (0,1)
# print(poz_1)
# #4.3615741232527263e-72
# print(poz_2)
# #-2.6183415306398385e+77

# # Tworzenie dwuwymiarowej tablicy (macierzy) 2x2
# #                   wynik:
# macierz = np.array([[1, 2],
#                     [3, 4]])
# print(macierz)
# # Tworzenie jednowymiarowej tablicy z wartościami od 1 do 2 z krokiem 0.1
# liczby = np.arange(1, 2, 0.1)  # ostatnie to krok
# print(liczby) #w:[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
#
# # Tworzenie jednowymiarowej tablicy z 5 równomiernie rozłożonymi
# # wartościami między 1 a 2 (inclusive)
# liczby_lin = np.linspace(1, 2, 5)  # ostatnie to ilosc elementow
# # w: [1.   1.25 1.5  1.75 2.  ]
# print(liczby_lin)
# liczby_lin = np.linspace(1, 2, 5,endpoint=False) #ostatnie jest odpowiedzialne z a to ze przedzial jest otwarty
# # w:# [1.  1.2 1.4 1.6 1.8]
# print(liczby_lin)

# # Tworzenie tablicy z indeksami o kształcie 5x3 (tablica trójwymiarowa)
# z=np.indices((5,3)) #macierz 3 wymiarowa
# print(z)
# # Wynik:
# # [[[0 0 0]
# #   [1 1 1]
# #   [2 2 2]
# #   [3 3 3]
# #   [4 4 4]]
# #
# #  [[0 1 2]
# #   [0 1 2]
# #   [0 1 2]
# #   [0 1 2]
# #   [0 1 2]]]
#
# # Wyświetlenie pierwszej macierzy (zawierającej indeksy wierszy)
# print(z[0])#dostawanie sie do indexu 3 wymiarowego(moje)
# # Wynik:
# # [[0 0 0]
# #  [1 1 1]
# #  [2 2 2]
# #  [3 3 3]
# #  [4 4 4]]
#
# # Pobranie wartości z pierwszej macierzy (zawierającej indeksy wierszy)
# # z pozycji w wierszu 3, kolumnie 1
# print(z[0,3,1])# tablica, wiersz, indeks kolumny(: 0-pierwsza macierz,1-druga macierz)
# # w: 3

# # Tworzenie dwóch macierzy x i y z indeksami w zakresie od 0 do 4 w obu wymiarach
# # Funkcja np.mgrid tworzy siatkę współrzędnych,
# x,y=np.mgrid[0:5,0:5]#tworzy 2 macierze ale kazda do odzielnej zmiennej
# print(x) #indeksy wiersz w przestrzeni dwuwymiarowej
# print(y) #indeksy kolumn w przestrzeni dwuwtmiarowej
# # Wynik dla x:
# # [[0 0 0 0 0]
# #  [1 1 1 1 1]
# #  [2 2 2 2 2]
# #  [3 3 3 3 3]
# #  [4 4 4 4 4]]
# # Wynik dla y:
# # [[0 1 2 3 4]
# #  [0 1 2 3 4]
# #  [0 1 2 3 4]
# #  [0 1 2 3 4]
# #  [0 1 2 3 4]]
# # Tworzenie macierzy diagonalnej z wartościami od 0 do 4 na głównej przekątnej
# mat_diag_k=np.diag([a for a in range(5)]) #tworzy mcierz  z ta petla na peatnej
# # Wynik:
# # [[0 0 0 0 0]
# #  [0 1 0 0 0]
# #  [0 0 2 0 0]
# #  [0 0 0 3 0]
# #  [0 0 0 0 4]]
# mat_diag_k=np.diag([a for a in range(5)],k=-1) #tworzy mcierz  z ta petla na przekatnej=k-1 czyli przesunie sie o 1 do dolu
# print(mat_diag_k)
#
# # Tworzenie jednowymiarowej tablicy z wartościami od 0 do 4 przy użyciu iteratora
# z=np.fromiter(range(5),dtype='int32') # fromiter zwraca same wektory, koniecznie z obiektu iterowanego
# print(z)# w:[0 1 2 3 4]

# # Tworzenie ciągu bajtów i konwersja do tablicy jednowymiarowej
# # przy użyciu dtype='S1' (pojedyncze znaki)
# znaki = b'abcdef'  # b onqacza ze napis jest przekazywany jako ciag bajtow
# zn1 = np.frombuffer(znaki, dtype='S1')  # po 1 znaku jako pojedynczy element tablicy
# print(zn1)#w: [b'a' b'b' b'c' b'd' b'e' b'f']
# # Tworzenie ciągu bajtów i konwersja do tablicy jednowymiarowej
# # przy użyciu dtype='S3'(trójznakowe fragmenty)
# zn2 = np.frombuffer(znaki, dtype='S3')  # zawsze na równe części musi być podzielone, bo jak nie to error
# print(zn2)
# #w: [b'abc' b'def']

# znaki = 'abcdefg'
# # Tworzenie tablicy NumPy z każdym znakiem jako osobny element,
# # typ danych domyślny
# zn3 = np.array(list(znaki))#w: ['a' 'b' 'c' 'd' 'e' 'f' 'g']
# # Tworzenie tablicy NumPy z każdym znakiem jako osobny element,
# # typ danych: string
# zn4 = np.array(list(znaki), dtype='S1') #w [b'a' b'b' b'c' b'd' b'e' b'f' b'g']
# # Tworzenie tablicy NumPy z każdym znakiem jako osobny element,
# # typ danych: bajty
# zn5 = np.array(list(b'abcdef'))#w: [ 97  98  99 100 101 102]
# # Tworzenie tablicy NumPy z każdym znakiem jako osobny element,
# # typ danych: string
# zn6 = np.fromiter(znaki, dtype='S1')  # string, dl calego znaku
# #w: [b'a' b'b' b'c' b'd' b'e' b'f' b'g']
# # Tworzenie tablicy NumPy z każdym znakiem jako osobny element,
# # typ danych: Unicode
# zn7 = np.fromiter(znaki, dtype='U1')#w ['a' 'b' 'c' 'd' 'e' 'f' 'g']
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)


# #dzialnia na macierzach dziaja sie miejscami a nie jak!!!
# mat=np.ones((2,2))
# mat_1=np.ones((2,2))
# # Dodawanie dwóch macierzy element po elemencie
# print(mat+mat_1)#Wynik: [[2. 2.], [2. 2.]]
# # Odejmowanie jednej macierzy od drugiej element po elemencie
# print(mat-mat_1)# Wynik: [[0. 0.], [1. 1.]]
# # Mnożenie dwóch macierzy element po elemencie
# print(mat*mat_1)# Wynik: [[1. 1.], [1. 1.]]
# # # Dzielenie jednej macierzy przez drugą element po elemencie
# print(mat/mat_1) # Wynik: [[1. 1.], [1. 1.]]
# # Przypisanie nowych wartości do macierzy mat_1
# mat_1=np.array([[3, 5],[5, 4]])
# print(mat_1)
# # Mnożenie macierzy element po elemencie
# print(mat*mat_1)# Wynik: [3, 5],[5, 4]


# #wycinki z wektorow
# a=np.arange(10)# Wynik: [0 1 2 3 4 5 6 7 8 9]
# print(a)
# # Tworzenie wycinka (slice) zaczynającego się od indeksu 2 do indeksu 7
# # (exclusive) z krokiem 2
# s=slice(2,7,2)
# print(a[s])# Wynik: [2 4 6]
# # Tworzenie obiektu range zaczynającego się od 2 do 7
# # (exclusive) z krokiem 2
# s=range(2,7,2)# Wynik: [2 4 6]
# # Wyświetlenie elementów wektora a wybranych przez obiekt range s
# print(a[s])# Wynik: [2 4 6]
# # Wybór elementów wektora a od indeksu 2 do 7 (exclusive) z krokiem 2
# print(a[2:7:2])# Wynik: [2 4 6]
# # Wybór elementów wektora a od indeksu 1 do końca
# print(a[1:])#wyswitalam wszytsko z tablic a od elementu 1 do konca
# # Wynik: [1 2 3 4 5 6 7 8 9]
# # Wybór elementów wektora a od indeksu 2 do 5 (exclusive)
# print(a[2:5]) #od do
# # Wynik: [2 3 4]

# #na macierzach
# # Tworzenie wektora od 0 do 24 (włącznie)
# mat=np.arange(25)#wektor
# # Zmiana kształtu wektora na macierz o wymiarach 5x5
# mat=mat.reshape((5,5))#tworzy z nieg macierz 5 na 5
# print(mat)
# """
# Wynik:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
# """
# # Wybór wierszy od drugiego wiersza do ostatniego
# print(mat[1:])
# """
# Wynik:
# [[ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
# """
# # Wybór kolumny drugiej
# print(mat[:,1])# Wynik: [ 1  6 11 16 21]
# # Wybór dwóch ostatnich kolumn
# # Wybór dwóch ostatnich kolumn
# print(mat[:,-2:])
# """
# Wynik:
# [[ 3  4]
#  [ 8  9]
#  [13 14]
#  [18 19]
#  [23 24]]
# """
#
# # Wybór wierszy od 3(o indexsie 2) do ostatniego 5(czyli 6 wyłacznie 6-1=5)
# # i kolumn od 2(o indexie 1) do 3 (o indexie 2 bo 3-1=2 wyłacznie)
# print(mat[2:6,1:3])#od wiersza o indexsie 2 i biore wiersze
# """
# Wynik:
# [[11 12]
#  [16 17]
#  [21 22]
# """
# # Wybór wszystkich wierszy i kolumn o indeksach 2 i 4 (3 i 5)
# print(mat[:,range(2,6,2)])#wyciecie po indeksach kolum
# # caloosci od 2 do konca wylacznie z krokiem 2
# """
# Wynik:
# [[ 2  4]
#  [ 7  9]
#  [12 14]
#  [17 19]
#  [22 24]]
# """

# x=np.array([[0,1,2],
#             [3,4,5],
#             [6,7,8],
#             [9,10,11]])
# print(x)
# # Określenie indeksów dla wierszy i kolumn dla naroznikow macierzy
# rows=np.array(([0,0],[3,3]))
# cols=np.array(([0,2],[0,2]))
# # Wybór elementów z naroznikow macierzy x
# # na podstawie podanych indeksow
# y=x[rows,cols]
# print(y)#wyswietlnie elemntow ktore sie znajduja w tych naroznikach
#
# print(sys.version)
