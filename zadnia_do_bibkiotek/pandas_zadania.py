import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
# liczba_urodzen_w_latach=df.groupby(['Rok']).agg({'Liczba':['sum']})
# lata=list(df['Rok'].unique())#szuka unikalnych wartosci w kolumni erok
# urodzenia=np.array(liczba_urodzen_w_latach)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.plot(lata,urodzenia)
# plt.xticks(lata,rotation=45)
# plt.xlabel("liczba")
# plt.ylabel("urodzenia")
# plt.title("Urodzenia na przestrzeni lat")
# plt.show()
# Zadanie 2
# # Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
# #moje:
# mezczyzni=df[df['Plec']=='M']
# liczba_mezczyzni=mezczyzni['Liczba'].sum()
# kobiety=df[df['Plec']=='K']
# liczba_kobiet=kobiety['Liczba'].sum()
# ilosc=[liczba_kobiet,liczba_mezczyzni]
# plcie=['kobiety','mezczyzni']
# sumy=[liczba_kobiet,liczba_mezczyzni]
# plt.bar(plcie,sumy)
# plt.show()
#od:
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title("Liczba urodzonych chłopców i dziewczynek")
# plt.show()

# # Zadanie 3
# # Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5
# # latach z datasetu.
# ostatnie_5_lata=df[df['Rok']>2012].groupby(['Plec']).agg({'Liczba':'sum'})
# wykres=ostatnie_5_lata.plot.pie(subplots=True,autopct='%.2f%%',fontsize=20)
# plt.legend()
# plt.show()

# Zadanie 4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych
# sprzedawców (zbiór danych zamówienia.csv).
df = pd.read_csv('zamowienia.csv', delimiter=';')
policzone = df.groupby('Sprzedawca').size()
policzone.plot.bar()
plt.ylabel("liczba zamówień")
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title('Ilość zamówień sprzedawców')
plt.show()
#.size() zwraca rozmiar każdej grupy, czyli liczbę wierszy przypadających
# na każdą grupę. Daje to liczbę wystąpień każdej unikalnej wartości w kolumnie 'Sprzedawca'