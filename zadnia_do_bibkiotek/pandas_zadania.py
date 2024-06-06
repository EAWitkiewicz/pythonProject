import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
liczba_urodzen_w_latach=df.groupby(['Rok']).agg({'Liczba':['sum']})
lata=list(df['Rok'].unique())
urodzenia=np.array(liczba_urodzen_w_latach)
plt.plot(lata,urodzenia)
plt.tight_layout
plt.xticks(lata,rotation=45)
plt.xlabel("liczba")
plt.ylabel("urodzenia")
plt.title("Urodzenia na przestrzeni lat")
plt.show()
# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5
# latach z datasetu.
# Zadanie 4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych
# sprzedawców (zbiór danych zamówienia.csv).