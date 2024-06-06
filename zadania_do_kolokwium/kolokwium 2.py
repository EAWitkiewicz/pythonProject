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
dane=pd.read_csv('automobile.csv',sep=';',decimal='.',header=0)

#Utwórz i wyświetl nową ramkę danych składającą się z rekordów dla
# samochodów audi i dodge.
audi_doge=dane[(dane['Car model']=='audi') | (dane['Car model']=='dodge')]
print(audi_doge)
#Na nowej ramce danych dokonaj grupowania danych po kolumnie „Car model”
# a następnie policz sumę wartości dla tych samochodów (kolumna Price)
modele=dane.groupby(['Car model'])
suma_cen=modele['Price'].sum()
print(suma_cen)
#Na podstawie utworzonej grupy utwórz wykres słupkowy, dodaj tytuł oraz
# etykiety dla osi x i y. Dopasuj rozmiar wykresu tak aby był on widoczny w całości.
auta=np.array(list(modele.groups.keys()))
ceny=list(suma_cen)
print(ceny)
fig,ax=plt.subplots()
color=plt.cm.viridis(np.linspace(0,1),len(auta))
ax.bar(x=auta,height=ceny,color=color)
plt.title('Ceny aut')
plt.xlabel('Modele aut')
plt.ylabel('Cena ')
plt.xticks(rotation=45,ha='right')
plt.subplots_adjust(bottom=0.3,left=0.15)
#plt.legend()
plt.show()
#Zad 3. (6pkt) Za pomocą biblioteki pomocą pandas wczytaj zawartość pliku
# „automobile.csv” do ramki danych i  utwórz wykres kołowy przedstawiający
# procentową ilość samochodów z danym rodzajem paliwa (kolumna Fuel-type).
# Procentowe wartości mają być zaokrąglone do dwóch miejsc po przecinku,
# rozmiar czcionki 14. Dodaj tytuł i legendę.

# Policz ilość samochodów dla każdego rodzaju paliwa
ile=dane['Fuel type'].value_counts()

fig,ax=plt.subplots()
ax.pie(ile,labels=ile.index,autopct='%2.f',fontsize=14)
plt.show()
