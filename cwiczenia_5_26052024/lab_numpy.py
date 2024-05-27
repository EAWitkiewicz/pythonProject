import numpy as np
import numpy as ny

#WEKTORY
# a=ny.array([20,30,40,50])
# b=ny.arange(4)
#
# print(a)
# print(b)
#
# c=a-b
# print(b**2)
#print(c)

#print(b**2)

# print(a)
# a+=b
# print(a)
# a-=b
# print(a)

#MNOZENIE WEKTORÓW
#d=a*b
#print("\n",d,"\n")


# b=ny.array(3)
# print(b)
# print(ny.exp(b))
# print(ny.sqrt(b))
# c=ny.array([2.,-1,4.])
# print(ny.add(b,c))

#MNOZENIE MACIERZY
# a=ny.arange(3)
# b=ny.arange(3)
# print(a)
# print(b)
# print(a.dot(b))
# print(ny.dot(a,b))
# c=ny.array([[1,5],[2,6],[7,4]])
# d=ny.array([[2,5,4],[4,3,1]])
#
#seweryna::
# print("Macierz c: ", c, "\n")
# print("Macierz d: ",d, "\n")
# print("Wynik mnozenia macierzy c * d: ", np.dot(c,d), "\n")
#K.s

# print(c)
# print(d)
# print(ny.dot(c,d))
# print(ny.dot(d,c))

#SUMA ELEMENTÓW MACIERZY
# a=np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.min(axis=1))
# print(a.cumsum(axis=1))


#PETLE NA MACIERZACH
# a=np.arange(6).reshape((3,2))
# print(a)
# for b in a: #element b, bedzie jako pojedynczy wiersz
#     print(b)
#
# a=ny.arange(6).reshape((3,2))
# print(a)
# for b in a.flat:#.flat splaszcza macierz do wektora
#     print(b)
#
# print(a)
# for b in a:#dostep do kazdego elementu z wiersza oddzielnie
#     for i in range(len(b)):
#         print(b[i],end=' ')
#         print()
# print(a)
#
# a=ny.arange(6).reshape((3,2))
# print(a)
# print(a.shape)
# print(type(a))
# for i in range(0,a.shape[0]):#.shape[0] - odwolanie sie do pozycji zerowej swojego rezultatu
#     for j in range(0,a.shape[1]):#.shape[1] - wartosc odp. za ilosc kolumn, w tym przypadku 2 kolumny
#         print(a[i][j],end=' ')
#     print(" ")
#
# #PRZEKSZTALCANIE MACIERZY
# a=ny.arange(6)
# print(a)
# print(a.shape)
# print("")
# b=a.reshape((2,3))
# print(b)
# print(b.shape)
# print("")
# c=b.reshape((3,2))
# print(c)
# print(c.shape)
# print("")
# #Metoda ravel odtwarza wektor wejsciowy, splaszcza macierz do rozmiarow 1 na x elementow
# d=c.ravel()
# print(d)
# print(d.shape)
# print("")

# #TRANSPOZYCJA MACIERZY
# e=b.T
# print(e)
# print(e.shape)


# CO DO NUMPY TO TYLE
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belhia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brazylia'],
        'Populacja': [11190846, 13031171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')
print(df)
df.to_csv('plik.csv', index=False)

print(s['c'])
print(s.c)
print(df[0:1])
print("")
print(df['Populacja'])
print(df.iloc[0.0])
print(df.loc[0, "Kraj"])
print(df.a[0, "Kraj"])
print('kraj' + df.Kraj)
print(df.sample())
