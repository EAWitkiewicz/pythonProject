import sys
import numpy as np

a = np.array([0, 1])
print(a)

a = np.arange(2)  # petla od i=0 do i=2
print(a)
print(type(a))

print(a.dtype)  # typ elementow jakie tablica przchowuje

a = np.arange(2, dtype='int32')
print(a.dtype)
b = a.astype('float')  # w kopi inty sa zamieniane na foaty
print(b)
print(b.dtype)
print(b.shape)

print(a.ndim)  # ile wymiarowa tablica

m = np.array((np.arange(2), np.arange(2)))  # tworzenie tablicy dwowymiaorwej z dwoma elementami w wierszu
print(m)
print(m.shape)
print(m.ndim)
m2 = np.array([[2, 3, 5], [2, 4, 6]])
print(m2)
print(m2.shape)
wektor = np.arange(5)
print(wektor)

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2, 2))
print(pusta)
poz_1 = pusta[1, 1]  # index wiersza index kolumny
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

macierz = np.array([[1, 2],
                    [3, 4]])
print(macierz)
liczby = np.arange(1, 2, 0.1)  # ostatnie to krok
print(liczby)

liczby_lin = np.linspace(1, 2, 5)  # ostatnie to ilosc elementow
liczby_lin = np.linspace(1, 2, 5,endpoint=False) #ostatnie jest odpowiedzialne z a to ze przedzial jest otwarty
print(liczby_lin)

z=np.indices((5,3)) #macierz 3 wymiarowa
print(z)
print(z[0])#dostawanie sie do indexu 3 wymiarowego
print(z[0,3,1])#tablica wiersz index kolumny 0-pierwsza macierz/1-druga macierz

x,y=np.mgrid[0:5,0:5]#tworzy 2 macierze ale kazda do odzielnej zmiennej
print(x)
print(y)

mat_diag_k=np.diag([a for a in range(5)]) #tworzy mcierz  z ta petla na
mat_diag_k=np.diag([a for a in range(5)],k=-1) #tworzy mcierz  z ta petla na przekatnej=k-1 czyli przesunie sie o 1 do dolu
print(mat_diag_k)

z=np.fromiter(range(5),dtype='int32') #fromiter zwraca same wektory,koniecnie z objektu iterowanego
print(z)







print(sys.version)
