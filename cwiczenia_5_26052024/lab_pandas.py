import sys
import math
import random
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])  #np.nan - odzwierciedlenie pustego weirsza z bazy danych
print(s)
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela' , 'New Delphi', 'Braslia'],
        'Populacja' : [191129123, 123213213, 23123123]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)

df = pd.read_csv('dane.csv', header=0, sep=';',decimal=',')     #Zaimportowanie pliku .csv, donyslnie separator to , a przy liczbach dziesietnych .
print(df)
df.to_csv('plik.csv', index=False)                                  #Zapisz do pliku

print(s['c'])
print(s.c)  #ODNIESIENIE SIE DO ELEMENTU, LEPIEJ ODNIESC SIE W []
print(df[0:1])  #Dostep do pojedynczych elementow, - wycinanie
print("")
print(df["Populacja"]) #Odniesienie sie do kolumny
print(df.iloc[0, 0])    #Wysiwetlenie pojedynczego elementu w ramce danych
print(df.loc[0, "Kraj"]) #wybieram numer indekus wiersza i nazwe kolumny
print(df.at[0, "Kraj"]) #wybieram numer indekus wiersza i nazwe kolumn
print('kraj' + df.Kraj)
print(df.sample())