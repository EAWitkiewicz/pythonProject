import sys
import math
import random
import numpy as np
import pandas as pd
# Tworzenie serii Pandas z wartościami liczbowymi i wartością NaN
s = pd.Series([1, 3, 5, np.nan, 6, 8])  #np.nan - odzwierciedlenie pustego weirsza z bazy danych
print(s)
#wynik:
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
#dtype: float64
#tworzenie kolejnej serii ,zamiast nr wierszy bedzie a,b,c,d
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
#Wynik:
# a    10
# b    12
# c     8
# d    14
# dtype: int64
print("____________________________________________________________")
# Tworzenie słownika z listami wartości
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela' , 'New Delphi', 'Braslia'],
        'Populacja' : [191129123, 123213213, 23123123]}
# Tworzenie DataFrame Pandas z słownika
df = pd.DataFrame(data)
print(df)
#wynik:
#        Kraj     Stolica  Populacja
# 0    Belgia    Bruksela  191129123
# 1     Indie  New Delphi  123213213
# 2  Brazylia     Braslia   23123123
# Wyświetlanie typów danych kolumn DataFrame
print(df.dtypes)
#wynik:
# Kraj         object
# Stolica      object
# Populacja     int64
# dtype: object
print("____________________________________________________________")

#wczytywanie dnaych z pliku z rezszerzeniem csv.
#header=0 oznacza, że pierwsza linia pliku CSV zawiera nazwy kolumn.
#sep=';' oznacza, że średnik (;) jest używany jako separator pól w pliku CSV.
# decimal=',' oznacza, że przecinek (,) jest używany jako separator dziesiętny w pliku CSV.
#ODKOMENTOWAC!!!!!!!!!
#df = pd.read_csv('dane.csv', header=0, sep=';',decimal=',')     #Zaimportowanie pliku .csv, donyslnie separator to , a przy liczbach dziesietnych .
print(df)
#wynik:
#    Imię i nazwisko        Data Wartość zamówienia
# 0  Marek Michalski  10.01.2018             1200.0
# 1  Marek Michalski  21.01.2018              456.5
# 2    Alan Strzygło  22.01.2018              350.0
# 3  Marek Michalski  23.01.2018              800.0
# 4    Alan Strzygło  24.01.2018              349.0
# 5    Alan Strzygło  26.01.2018             1350.0
#z takiego pliku:
# Imię i nazwisko;Data;Wartość zamówienia
# Marek Michalski;10.01.2018;1200.0
# Marek Michalski;21.01.2018;456.5
# Alan Strzygło;22.01.2018;350.0
# Marek Michalski;23.01.2018;800.0
# Alan Strzygło;24.01.2018;349.0
# Alan Strzygło;26.01.2018;1350.0

#zapisuje DataFrame do pliku CSV.
#index=False oznacza, że indeksy wierszy nie powinny być zapisywane do pliku CSV
# tworzy nowy plik o nazwie plik.csv.Jeśli plik o tej nazwie już istnieje, zostanie nadpisany.
df.to_csv('plik.csv', index=False)
#wynik w nowp zapisanym pliku:
# Imię i nazwisko,Data,Wartość zamówienia
# Marek Michalski,10.01.2018,1200.0
# Marek Michalski,21.01.2018,456.5
# Alan Strzygło,22.01.2018,350.0
# Marek Michalski,23.01.2018,800.0
# Alan Strzygło,24.01.2018,349.0
# Alan Strzygło,26.01.2018,1350.0

print(s['c'])#wartość elementu z indeksem 'c' w serii s.
#w: 8
#wartość elementu z indeksem 'c' w serii s.
print(s.c)  #ODNIESIENIE SIE DO ELEMENTU, LEPIEJ ODNIESC SIE W []
#w: 8
#dostep do pierwszy wiersz z DataFrame df
#skad[od:do(wyłacznie)]
print(df[0:1])  #Dostep do pojedynczych elementow, - wycinanie
#wynik:
#      Kraj   Stolica  Populacja
# 0  Belgia  Bruksela  191129123
print("")
print(df["Populacja"]) #Odniesienie sie do kolumny
#wynik:
# 0    191129123
# 1    123213213
# 2     23123123

print(df.iloc[0, 0])    #Wysiwetlenie pojedynczego elementu w ramce danych
#w:Belgia
print(df.loc[0, "Kraj"]) #wybieram numer indekus wiersza i nazwe kolumny
#w:Belgia
print(df.at[0, "Kraj"]) #wybieram numer indekus wiersza i nazwe kolumn
#w:Belgia
# iloc: Wybiera elementy oparte na liczbowych indeksach wierszy i
# kolumn. Najszybsza, ale najmniej elastyczna.
#
# loc: Wybiera elementy oparte na etykietach wierszy i kolumn.
# Może obsługiwać zarówno etykiety liczbowe, jak i napisowe. Bardziej elastyczna, ale wolniejsza niż iloc.
#
# at: Podobna do loc, ale może wybierać tylko pojedyncze elementy
# jednocześnie. Najszybsza, gdy masz do czynienia z liczbowymi
# indeksami wierszy i kolumn.

print('kraj' + df.Kraj)#łaczy napisy ,df.Kraj wyswietliloby same nazwy krajow
#wyniki:
# 0      krajBelgia
# 1       krajIndie
# 2    krajBrazylia
# Name: Kraj, dtype: object

# jeden losowy element
print(df.sample())
#przykladowy wynik:
#        Kraj  Stolica  Populacja
# 2  Brazylia  Braslia   23123123

#cwiczenia 01.06.2024
#dostep do poszczefolnych parametyrowa za pomoca trzch parametrowe
#http://wmii.uwm.edu.pl/~cezary/WD/cw8.pdf
# Losuje 2 wiersze z DataFrame df bez powtórze
print(df.sample(2))
# Losuje 50% wierszy z DataFrame df bez powtórzeń.
print(df.sample(frac=0.5))
# Losuje 10 wierszy z DataFrame df z powtórzeniami.
# Parametr replace jest ustawiony na True,
# co pozwala na duplikaty w wylosowanej próbce.
print(df.sample(n=10,replace=True))

# Działanie: Wyświetla pierwsze kilka wierszy DataFrame.
# Domyślna liczba wierszy: 5
# Składnia: df.head(n)
# n: Liczba wierszy do wyświetlenia.
print(df.head())
#Wyświetla pierwsze 2 wiersze DataFrame df.
print(df.head(2))

# Działanie: Wyświetla ostatni wiersz DataFrame df.
# Składnia: df.tail(n)
# n: Liczba wierszy do wyświetlenia.
print(df.tail(1))

# Działanie: Wyświetla podsumowanie statystyczne liczbowe DataFrame, w tym:
# Liczbę wierszy
# Średnią, medianę, minimum, maksimum i odchylenie standardowe każdej kolumny liczbowej
# Liczbę wartości niezerowych dla każdej kolumny
#w kolumnach z wartosciami liczbowymi
print(df.describe())
#wynik:
#           Populacja
# count  3.000000e+00
# mean   1.124885e+08
# std    8.451490e+07
# min    2.312312e+07
# 25%    7.316817e+07
# 50%    1.232132e+08
# 75%    1.571712e+08
# max    1.911291e+08

print(df.T)#transpozycja rami danych zamian awierszy z kolumnami
#wynik:
#                    0           1         2
# Kraj          Belgia       Indie  Brazylia
# Stolica     Bruksela  New Delphi   Braslia
# Populacja  191129123   123213213  23123123

# filtruje serię s, zwracając tylko te elementy, które są
# większe niż 9. W wyniku otrzymasz serię z wartościami spełniającymi ten warunek.
print(s[(s>9)])
#where zwraca serię, w której wartości spełniające warunek (większe niż 10)
# pozostają bez zmian, a wartości niespełniające warunku są zastępowane przez NaN.
print(s.where(s>10))
#to samo tylko zamiast NaN wypisauje ,,za duze"
print(s.where(s>10,'za duze'))
#seria=s.copy(): Tworzy kopię serii s i przypisuje ją do zmiennej seria.
# Dzięki temu oryginalna seria s pozostaje niezmieniona.
seria=s.copy()
#Gdyby inplace=True nie było użyte, operacja where zwróciłaby nową
# serię z wprowadzonymi zmianami, a oryginalna seria seria pozostałaby
# niezmieniona.
seria.where(seria>10,'za duze',inplace=True)
print(seria)
#wyniki:
# a    za duze
# b         12
# c    za duze
# d         14
# Filtrowanie serii s, zwracając tylko te elementy, które są mniejsze
# lub równe 10. Operator ~ neguje warunek (s>10), co oznacza, że
# zwracane są elementy niespełniające warunku s>10.
print(s[~(s>10)])
#wynik:
# a    10
# c     8
# dtype: int64
#Filtrowanie wartości większych niż 8 i mniejszych niż 13:
print(s[(s<13)&(s>8)])
#wynik:
# a    10
# b    12
# dtype: int64

#Filtrowanie DataFrame df, zwracając tylko te wiersze, gdzie wartość w
# kolumnie "Populacja" jest większa niż 1000 i indeks wiersza jest 0 lub 2.
print(df[(df.Populacja>1000)&(df.index.isin([0,2]))])
#df.index.isin([0, 2]): Tworzy maskę (warunek logiczny),
# która zwraca True dla wierszy, których indeksy są w liście [0, 2].
#wynik:
#        Kraj   Stolica  Populacja
# 0    Belgia  Bruksela  191129123
# 2  Brazylia   Braslia   23123123

#zwraca te wiersze z data freame'a gdzei jest brazylia i belgia
szukaj=['Belgia','Braslia']
print(df.isin(szukaj))#w takiej formie gdzie jest tylko true i false
#wynik:
#     Kraj  Stolica  Populacja
# 0   True    False      False
# 1  False    False      False
# 2  False     True      False

#dodawnie nowych elementow trocher tj w slowniku
# Dodaje nowy element do serii s z indeksem 'e' i wartością 15.
# nowy element zostanie dodany do końca seri
s['e']=15
print(s.e)#wynik: 15
s['f']=16#dodaje nowy element o idexie f i wartosci 16
print(s)
#wybik:
# a    10
# b    12
# c     8
# d    14
# e    15
# f    16

#nowy wiersz najlepiej dodac w formie listy kolumn
df.loc[3]='dodane'# Dodaje nowy wiersz z indeksem 3 do DataFrame,
# wypełniając wszystkie komórki wiersza wartością 'dodane'.
print(df)
#wynik:
#        Kraj     Stolica  Populacja
# 0    Belgia    Bruksela  191129123
# 1     Indie  New Delphi  123213213
# 2  Brazylia     Braslia   23123123
# 3    dodane      dodane     dodane
df.loc[4]=['Polska','Warszawa',38575467]#dodaje nowe dane w formie listy
print(df)
#wynik:
# 0    Belgia    Bruksela  191129123
# 1     Indie  New Delphi  123213213
# 2  Brazylia     Braslia   23123123
# 3    dodane      dodane     dodane
# 4    Polska    Warszawa   38575467

new_df=df.drop([3])#zwraca ramke danych jako kopie bez usunietego elementu
print(new_df)
#wynik:(bez 3 wiersza)
#        Kraj     Stolica  Populacja
# 0    Belgia    Bruksela  191129123
# 1     Indie  New Delphi  123213213
# 2  Brazylia     Braslia   23123123
# 4    Polska    Warszawa   38575467

#Usuwanie wiersza w miejscu (bez tworzenia kopii):
df.drop([3],inplace=True)
print(df)
#wunik:
#        Kraj     Stolica  Populacja
# 0    Belgia    Bruksela  191129123
# 1     Indie  New Delphi  123213213
# 2  Brazylia     Braslia   23123123
# 4    Polska    Warszawa   38575467


#axis decyduje po czym jest uswanie dany element  (1-kolumny,0-wiersze)
#df.drop('Kraj',axis=1,inplace=True) do odkomentowania
print(df)
#wynik:
#       Stolica  Populacja
# 0    Bruksela  191129123
# 1  New Delphi  123213213
# 2     Braslia   23123123
# 4    Warszawa   38575467

# Dodawanie nowej kolumny:
df['Kontynent']=['Europa','Azja',
                 'Ameryka Poludniowa','Europa']
print(df)
#wynik:
#       Stolica  Populacja           Kontynent
# 0    Bruksela  191129123              Europa
# 1  New Delphi  123213213                Azja
# 2     Braslia   23123123  Ameryka Poludniowa
# 4    Warszawa   38575467              Europa

#sortuje wersze po kolumnie kraj alfebetycznie
print(df.sort_values(by='Kraj'))
#wynik:
#        Kraj     Stolica  Populacja           Kontynent
# 0    Belgia    Bruksela  191129123              Europa
# 2  Brazylia     Braslia   23123123  Ameryka Poludniowa
# 1     Indie  New Delphi  123213213                Azja
# 4    Polska    Warszawa   38575467              Europa
#grupowanie po kontynentach
grouped=df.groupby(['Kontynent'])
#Pobranie określonej grupy z DataFrameGroupBy:
print(grouped.get_group('Europa'))
#wynik:
#      Kraj   Stolica  Populacja Kontynent
# 0  Belgia  Bruksela  191129123    Europa
# 4  Polska  Warszawa   38575467    Europa

#~df.groupby(['Kontynent']): Grupuje wiersze w DataFrame według wartości w kolumnie 'Kontynent'.
#~agg({'Populacja':['sum']}): Wykonuje agregację danych dla każdej grupy.
# W tym przypadku używamy funkcji sum() do obliczenia sumy populacji dla każdego kontynentu.
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
#wynik:
#                     Populacja
#                           sum
# Kontynent
# Ameryka Poludniowa   23123123
# Azja                123213213
# Europa              229704590

#######WYKRESY
import matplotlib.pyplot as plt
#pd.Series(...): Tworzy obiekt Series z wygenerowanych losowych liczb.
ts=pd.Series(np.random.randn(1000))
print(ts)
#0     -0.778730
# 1     -1.234568
# 2     -1.358140
# 3     -0.495758
# 4     -0.636445
#          ...
# 995   -1.261950
# 996   -1.590856
# 997    0.895280
# 998   -1.649255
# 999    0.402885
#Length: 1000, dtype: float64

ts=ts.cumsum()#obliczanie skumulowanej sumy
print(ts)
# 0       0.748168
# 1       2.904257
# 2       2.525722
# 3       0.653068
# 4       1.153770
#          ...
# 995    25.741454
# 996    26.761460
# 997    26.310061
# 998    27.150879
# 999    27.274170
#Length: 1000, dtype: float64
ts.plot()#worzenie wykresu z wczesniej stworzonej wersji danych
plt.show()
grupa=df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa)
#Kontynent
# Ameryka Poludniowa   23123123
# Azja                123213213
# Europa              229704590
grupa.plot(
    kind='bar',          # Określa typ wykresu jako słupkowy (bar chart)
    xlabel='Kontynent',  # Ustawia etykietę osi X na 'Kontynent'
    ylabel='Mid',        # Ustawia etykietę osi Y na 'Mid'
    rot=0,               # Ustawia kąt obrotu etykiet osi X na 0 stopni (brak obrotu)
    legend=True,         # Wyświetla legendę na wykresie
    title='Populacja z podziałem na kontynenty'  # Ustawia tytuł wykresu
)
wykres=grupa.plot.bar()# Tworzenie wykresu słupkowego z obiektu 'grupa'
wykres.set_ylabel("Mdl")# Ustawienie etykiety osi Y na 'Mdl'
wykres.set_xlabel('Kontynent')# Ustawienie etykiety osi X na 'Kontynent'
wykres.tick_params(axis='x',labelrotation=0)
# Ustawienie parametrów osi X, w szczególności obrót etykiet na 0 stopni (poziomo
wykres.legend()# Włączenie legendy na wykresie
wykres.set_title('Populacja z podziałem na kontynenty')# Ustawienie tytułu wykresu na 'Populacja z podziałem na kontynenty'
#plt.xticks(rotation=0)
plt.savefig('wykres.png')# Zapisanie wykresu do pliku 'wykres.png'

plt.show()
# header=0 oznacza, że pierwsza linia pliku CSV zawiera nazwy kolumn.
df=pd.read_csv('dane.csv',header=0,sep=";",
               decimal=".")
print(df)
#Zwrocic jaki jest separator liczb dziesientych i co oddziala kolumny czy : ; czy  -

# Grupuje dane w DataFrame `df` według kolumny
# 'Imię i nazwisko' i sumuje wartości w kolumnie 'Wartość zamówienia' dla każdej grupy
grupa=(df.groupby(['Imię i nazwisko']).
       agg({'Wartość zamówienia':["sum"]}))
grupa.plot(kind='pie',# Tworzy wykres kołowy (pie chart) z sumy wartości zamówień dla każdej osoby.
           subplots=True,# subplots=True tworzy osobne wykresy dla każdej grupy.
           autopct='%.2f %%',# autopct='%.2f %%' wyświetla wartości procentowe na wykresie z dokładnością do dwóch miejsc po przecinku.
           fontsize=20,
           figsize=(6,6),# figsize=(6,6) ustawia rozmiar wykresu na 6x6 cali.
           colors=['red','green'])
# wykres=grupa.plot.pie(subplots=True,autopct='%.2f %%',
#                       fontsize=20,figsize=(6,6))
plt.legend(loc="lower right")# Dodaje legendę do wykresu i umieszcza ją w prawym dolnym rogu.
plt.title('Suma zamowien dla sprzedarzy')
plt.show()
#
#
ts=pd.Series(np.random.randn(1000))
ts=ts.cumsum()
# Tworzy ramkę danych na podstawie serii `ts`
# z jedną kolumną o nazwie 'wartosci'.
df=pd.DataFrame(ts,columns=['wartosci'])
print(df)
df['Średnia krocząca']=df.rolling(window=20).mean()
df.plot()
plt.legend()
plt.show()




