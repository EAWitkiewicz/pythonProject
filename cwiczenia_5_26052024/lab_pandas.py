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

#df = pd.read_csv('dane.csv', header=0, sep=';',decimal=',')     #Zaimportowanie pliku .csv, donyslnie separator to , a przy liczbach dziesietnych .
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
# jeden losowy element
print(df.sample())

#cwiczenia 01.06.2024
#dostep do poszczefolnych parametyrowa za pomoca trzch parametrowe
#http://wmii.uwm.edu.pl/~cezary/WD/cw8.pdf
# n losowych elementów
print(df.sample(2))
# ilość elementów procentowo - uwaga na zaokrąglanie
print(df.sample(frac=0.5))
# jeżeli potrzeba nam więcej próbek niż znajduje się w zbiorze i dopuszczamy duplikaty
# to możemy użyć parametru replace, który będzie losował z powtórzeniami
print(df.sample(n=10,replace=True))
# zamiast wyświetlać całą kolekcję możemy wyświetlić tylko określoną liczbę
#pierwszych lub ostatnich elementów
#R:5 pierwszych tail 5 ostatnich
print(df.head())
print(df.head(2))
print(df.tail(1))
print(df.describe())
print(df.T)#transpozycja rami danych zamian awierszy z kolumnami

print(s[(s>9)])
print(s.where(s>10))
print(s.where(s>10,'za duze'))
seria=s.copy()
# seria.where(seria>10,'za duze',inplace=True)
print("##########")
print(seria)

print(s[~(s>10)])

print(s[(s<13)&(s>8)])

print(df[(df.Populacja>1000)&(df.index.isin([0,2]))])

print("##########")
szukaj=['Belgia','Brasilia']
print(df.isin(szukaj))

#dodawnie nowych elementow trocher tj w slowniku
s['e']=15
print(s.e)
s['f']=16
print(s)

#nowy wiersz najlepiej dodac w formie listy *cos tam cos za syzbko mowil* kolumn
df.loc[3]='dodane'
print(df)
df.loc[4]=['Polska','Warszawa',38575467]
print(df)
###
new_df=df.drop([3])#zwraca ramke danych jako kopie bez usunietego elementu
print(new_df)

df.drop([3],inplace=True)
print(df)
##
#axis decyduje po czym jest uswanie dany element
# df.drop('Kraj',axis=1,inplace=True)
print(df)

df['Kontynent']=['Europa','Azja',
                 'Ameryka Poludniowa','Europa']
print(df)

print(df.sort_values(by='Kraj'))
grouped=df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))#utworzeni grupy po kolumnie kontynet i
# dokonanie agregacji i *za szybko mowil i nie powtorzyl*

#######WYKRESY
import matplotlib.pyplot as plt

ts=pd.Series(np.random.randn(1000))
ts=ts.cumsum()
print(ts)
ts.plot()
plt.show()
grupa=df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa)
grupa.plot(kind='bar',xlabel='Kontynent',ylabel='Mid',rot=0,
           legend=True,
           title='Populacja z podziałem na kontynenty')
wykres=grupa.plot.bar()
wykres.set_ylabel("Mdl")
wykres.set_xlabel('Kontynent')
wykres.tick_params(axis='x',labelrotation=0)
wykres.legend()
wykres.set_title('Populacja z podziałem na kontynenty')
#plt.xticks(rotation=0)
plt.savefig('wykres.png')

plt.show()

df=pd.read_csv('dane.csv',header=0,sep=";",
               decimal=".")
print(df)
#Zwrocic jaki jest separator liczb dziesientych i co oddziala kolumny czy : ; czy  -
grupa=(df.groupby(['Imię i nazwisko']).
       agg({'Wartość zamówienia':["sum"]}))
grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',
           fontsize=20,figsize=(6,6),colors=['red','green'])
# wykres=grupa.plot.pie(subplots=True,autopct='%.2f %%',
#                       fontsize=20,figsize=(6,6))
plt.legend(loc="lower right")
plt.title('Suma zamowien dla sprzedarzy')
plt.show()
#
#
ts=pd.Series(np.random.randn(1000))
ts=ts.cumsum()
df=pd.DataFrame(ts,columns=['wartosci'])
print(df)
df['Średnia krocząca']=df.rolling(window=20).mean()
df.plot()
plt.legend()
plt.show()




