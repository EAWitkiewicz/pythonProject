import pandas as pd
#Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w (pliku
# /datasets/imiona.xlsx)
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
#df.to_excel('wyniki.xlsx', sheet_name='arkusz pierwszy')
#print(df)

# # Zadanie 2
# # Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji
# # biblioteki Pandas):
# # • tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w
# # danym roku
# liczba_imion_wieksza_niz_1000=df[df['Liczba']>1000]
# print(liczba_imion_wieksza_niz_1000)

# # • tylko rekordy gdzie nadane imię jest takie jak Twoje
# moje_imie=df[df['Imie']=='ALICJA']#bedzie drugie bo pierwsze nie weszlo
# print(moje_imie)

# # • sumę wszystkich urodzonych dzieci w całym danym okresie,
# liczba=df['Liczba'].sum()
# print(liczba)

# • sumę dzieci urodzonych w latach 2000-2005
# w_latach_2000_2005=df[(df.Rok>=2000)&(df.Rok<=2005)]
# suma_dzieci_z2000_2005=w_latach_2000_2005['Liczba'].sum()
# print(suma_dzieci_z2000_2005)

# # • sumę urodzonych chłopców i dziewczynek,
# grupowanie_kobiet=df[df['Plec']=='K']
# suma_kobiet=grupowanie_kobiet['Liczba'].sum()
# grupowanie_mezczyzn=df[df['Plec']=='M']
# suma_mezczyzn=grupowanie_mezczyzn['Liczba'].sum()
# print("suma kobiet: ", suma_kobiet)
# print("suma mezczyn: ",suma_mezczyzn)
# print("suma wszystkich: ",suma_kobiet+suma_mezczyzn)


# # • najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# Grupowanie danych według roku i płci
# grupowanie_po_roku_plci=df.groupby(['Rok','Plec'])
# # Znajdowanie indeksów najbardziej popularnych imion w każdej grupie
# najwieksz_liczba_wystapien =grupowanie_po_roku_plci['Liczba'].idxmax()
# # Wybieranie wierszy z oryginalnych danych na podstawie tych indeksów
# najpopularnijsze_imiona=df.loc[najwieksz_liczba_wystapien]
# # Sortowanie wyników dla lepszej czytelności
# najpopularnijsze_imiona=najpopularnijsze_imiona.sort_values(by=['Rok','Plec'], ascending=False)
# print(najpopularnijsze_imiona)

# # • najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
# wybieranie_kobiet=df[df['Plec']=='K']
# grupowanie_imion_k=wybieranie_kobiet.groupby('Imie')['Liczba'].sum()
# najpopularnijsze_zenskie=grupowanie_imion_k.idxmax()
# print("najpopularneijszze zenskie",najpopularnijsze_zenskie)
# wybieranie_mezczyzn=df[df['Plec']=='M']
# grupowanie_imion_m=wybieranie_mezczyzn.groupby('Imie')['Liczba'].sum()
# najpopularnijsze_meskie=grupowanie_imion_m.idxmax()
# print("najpopularnijsze meskie: ",najpopularnijsze_meskie)
# ogolnie=df.groupby('Imie')['Liczba'].sum()
# najpopularnijsze=ogolnie.idxmax()
# print("najpopularnijszze imie: ",najpopularnijsze)

# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
df1=pd.read_csv('zamowienia.csv',sep=';',decimal='.',header=0)
print(df1)
# # • listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z
# # DataFrame)
# nazwiska=df1['Sprzedawca'].unique()
# print(nazwiska)
# # • 5 najwyższych wartości zamówień
# maxymalnezamowienia=df1.nlargest(5,'Utarg')
# print(maxymalnezamowienia)
# # • ilość zamówień złożonych przez każdego sprzedawcę
# ilosc_zamowien = df1['Sprzedawca'].value_counts()
# print(ilosc_zamowien)
# # • sumę zamówień dla każdego kraju
# suma_zamowien_dla_kraju=df1.groupby(['Kraj']).agg({'idZamowienia':'count'})
# print(suma_zamowien_dla_kraju)

# • sumę zamówień dla roku 2005, dla sprzedawców z Polski
df1['Data zamowienia']=pd.to_datetime(df1['Data zamowienia'])
w_roku_2005=df1[df1['Data zamowienia'].dt.year==2005]
sprzedawcy_z_polski=w_roku_2005[w_roku_2005['Kraj']=='Polska']
suma_zamowien=sprzedawcy_z_polski['idZamowienia'].count()
print(suma_zamowien)
#TODO
# • średnią kwotę zamówienia w 2004 roku,

# • zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku
# zamówienia_2005.csv
df1['Data zamowienia']=pd.to_datetime(df1['Data zamowienia'])
rok2004=df1[df1['Data zamowienia'].dt.year==2004]
rok2005=df1[df1['Data zamowienia'].dt.year==2005]
dane_za_2004=rok2004.to_csv('zamowienia_2004.csv')
dane_za_2005=rok2005.to_csv('zamowienia_2005.csv')