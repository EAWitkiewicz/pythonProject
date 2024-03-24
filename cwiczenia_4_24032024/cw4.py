import sys
import numpy as np

# a = np.array([0, 1])
# print(a)
#
# a = np.arange(2)  # petla od i=0 do i=2
# print(a)
# print(type(a))
#
# print(a.dtype)  # typ elementow jakie tablica przchowuje
#
# a = np.arange(2, dtype='int32')
# print(a.dtype)
# b = a.astype('float')  # w kopi inty sa zamieniane na foaty
# print(b)
# print(b.dtype)
# print(b.shape)
#
# print(a.ndim)  # ile wymiarowa tablica
#
# m = np.array((np.arange(2), np.arange(2)))  # tworzenie tablicy dwowymiaorwej z dwoma elementami w wierszu
# print(m)
# print(m.shape)
# print(m.ndim)
# m2 = np.array([[2, 3, 5], [2, 4, 6]])
# print(m2)
# print(m2.shape)
# wektor = np.arange(5)
# print(wektor)
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2, 2))
# print(pusta)
# poz_1 = pusta[1, 1]  # index wiersza index kolumny
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)
#
# macierz = np.array([[1, 2],
#                     [3, 4]])
# print(macierz)
# liczby = np.arange(1, 2, 0.1)  # ostatnie to krok
# print(liczby)
#
# liczby_lin = np.linspace(1, 2, 5)  # ostatnie to ilosc elementow
# liczby_lin = np.linspace(1, 2, 5,endpoint=False) #ostatnie jest odpowiedzialne z a to ze przedzial jest otwarty
# print(liczby_lin)
#
# z=np.indices((5,3)) #macierz 3 wymiarowa
# print(z)
# print(z[0])#dostawanie sie do indexu 3 wymiarowego
# print(z[0,3,1])#tablica wiersz index kolumny 0-pierwsza macierz/1-druga macierz
#
# x,y=np.mgrid[0:5,0:5]#tworzy 2 macierze ale kazda do odzielnej zmiennej
# print(x)
# print(y)
#
# mat_diag_k=np.diag([a for a in range(5)]) #tworzy mcierz  z ta petla na
# mat_diag_k=np.diag([a for a in range(5)],k=-1) #tworzy mcierz  z ta petla na przekatnej=k-1 czyli przesunie sie o 1 do dolu
# print(mat_diag_k)
#
# z=np.fromiter(range(5),dtype='int32') #fromiter zwraca same wektory,koniecnie z objektu iterowanego
# print(z)

# znaki = b'abcdef'  # b onqacza ze napis jest przekazywany jko ciag bajtow
# zn1 = np.frombuffer(znaki, dtype='S1')  # po 1 znau jako pojedynczy element tablicy
# print(zn1)
# zn2 = np.frombuffer(znaki, dtype='S3')  # zawsze na rowne czesci musi byc podzielone bo jak nie to erroe
# print(zn2)
#
# znaki = 'abcdefg'
# zn3 = np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))
# zn6 = np.fromiter(znaki, dtype='S1')  # string i dl calego znaku
# zn7 = np.fromiter(znaki, dtype='U1')  # w unicodzie
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)


# #dzialnia na macierzach dziaja sie miejscami !!!
# mat=np.ones((2,2))
# mat_1=np.ones((2,2))
# mat=mat+mat_1
# print(mat)
# print(mat-mat_1)
# print(mat*mat_1)
# print(mat/mat_1)
# mat_1=np.array([[3, 5],[5, 4]])
# print(mat_1)
# print(mat*mat_1)


#wycinki z wektorow
# a=np.arange(10)
# print(a)
# s=slice(2,7,2)
# print(a[s])
# s=range(2,7,2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])#wyswitalam wszytsko z tablic a od elementu 1 do konca
# print(a[2:5]) #od do

#na macierzach
# mat=np.arange(25)#wektor
# mat=mat.reshape((5,5))#tworzy z nieg macierz 5 na 5
# print(mat)
# print(mat[1:])
# print(mat[:,1])
# print(mat[:,-2:])
# print(mat[2:6,1:3])#od wiersza o indexsie 2 i biore wiersze
# print(mat[:,range(2,6,2)])#wyciecie po kolumnach 3 i 5
# print('')


x=np.array([[0,1,2],
            [3,4,5],
            [6,7,8],
            [9,10,11]])

#narozniki macierzy
print(x)
rows=np.array(([0,0],[3,3]))
cols=np.array(([0,2],[0,2]))
y=x[rows,cols]
print(y)

print(sys.version)
