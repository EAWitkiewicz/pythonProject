import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Zad 1. (6pkt.) Za pomocą biblioteki matplotlib utwórz wykres liniowy funkcji f(x) = sin(x) * x,
# dla x z przedziału [-3,3] z wartościami zmieniającymi się co 1/2. Ustaw zakres osi x na wartości -3 i 3,
# dodaj etykiety do osi x i y, ustaw tytuł wykresu.
os_x=np.arange(-3,3,0.5)
y=np.sin(os_x)*os_x
plt.plot(os_x,y)
plt.ylabel('os y')
plt.xlabel('os x')
plt.title('wykres sin(x)*x')
plt.show()
print(os_x)

#Zad 2. (8pkt.) Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku
# „automobile.csv” do ramki danych, a następnie:
#Utwórz i wyświetl nową ramkę danych składającą się z rekordów dla
# samochodów audi i dodge.

#Na nowej ramce danych dokonaj grupowania danych po kolumnie „Car model”
# a następnie policz sumę wartości dla tych samochodów (kolumna Price)

#Na podstawie utworzonej grupy utwórz wykres słupkowy, dodaj tytuł oraz
# etykiety dla osi x i y. Dopasuj rozmiar wykresu tak aby był on widoczny w całości.

#Zad 3. (6pkt) Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku
# „automobile.csv” do ramki danych i  utwórz wykres kołowy przedstawiający
# procentową ilość samochodów z danym rodzajem paliwa (kolumna Fuel-type).
# Procentowe wartości mają być zaokrąglone do dwóch miejsc po przecinku,
# rozmiar czcionki 14. Dodaj tytuł i legendę.