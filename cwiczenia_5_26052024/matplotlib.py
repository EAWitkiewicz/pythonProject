import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
##WYKRES 3
# # Tworzy wykres liniowy dla podanych wartości [1, 2, 3, 4].
# # Domyślnie wartości te są traktowane jako wartości na osi Y.
# plt.plot([1,2,3,4])
# plt.ylabel('jakies liczby')#etykieta osi y
# plt.show()

##WYKRES 2
# # Tworzy wykres z wartościami [1, 2, 3, 4] na osi X i [1, 4, 9, 16] na osi Y,
# # używając czerwonych kółek połączonych linią ciągłą
# plt.plot([1,2,3,4],[1,4,9,16],'ro-')
# #'r' oznacza czerwony (red).
# #'o' oznacza marker w kształcie kółka (circle marker)
# #'-' oznacza linię ciągłą (solid line)..
# # Ustawia zakres osi X na (0, 6) i osi Y na (0, 20)
# plt.axis((0,6,0,20))
# plt.show()

# #WYKRES 3
# # Rysowanie pierwszej serii danych jako czerwona linia
# plt.plot([1,2,3,4],[1,4,9,16],'r')
# # Rysowanie drugiej serii danych jako kółka bez linii (domyślnie kolor jest niebieski)
# plt.plot([1,2,3,4],[1,4,9,16],'o')
# # plt.axis((0,6,0,20)) to to samo co ponizej:
# plt.xlim(0,6)# Ustawienie limitów osi x od 0 do 6
# plt.ylim(0,20)# Ustawienie limitów osi y od 0 do 20
# plt.show()

# #WYKRES 4
# # Generowanie 100 punktów pomiędzy 0 a 2, równomiernie rozmieszczonych
# x=np.linspace(0,2,100)
# # Wykres funkcji liniowej y = x z etykieta "liniowa" w legedzie
# plt.plot(x,x,label="liniowa")
# # Wykres funkcji kwadratowej y = x^2
# plt.plot(x,x**2,label="kwadratowa")
# # Wykres funkcji sześciennej y = x^3
# plt.plot(x,x**3,label="szescienna")
# # Ustawianie etykiet osi
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# # Ustawianie tytułu wykresu
# plt.title('prosty wykres')
# # Dodawanie legendy do wykresu wyswietlnie legendy,jesli wczesniej
# #zadeklarowalam lebele przy fukcjach to do wyswietlenia legendy
# #moge uzyc tylko plt.legend() z pustym nawiasem
# plt.legend(labels=['liniowa','kwadratowa','szescienna'])#albo tak w odpowiedniej kolejnisci
# # Zapisywanie wykresu do pliku PNG
# plt.savefig('wykres matplot.png')
# plt.show()
# # Otwieranie zapisanego obrazu za pomocą PIL
# im1=Image.open('wykres matplot.png')# Otwiera zapisany plik PNG do dalszego przetwarzania.
# # Konwertowanie obrazu do formatu RGB
# im1=im1.convert('RGB')
# # Zapisywanie obrazu w formacie JPG
# im1.save('nowy.jpg')

# #WYKRES 5
# x=np.arange(0,10.1,0.1)# Tworzenie zakresu wartości od 0 do 10 z krokiem 0.1
# # Obliczanie wartości funkcji sinus dla wszystkich elementów w x
# s=np.sin(x)#tworzy sinusoide
# plt.plot(x,s,label="sin(x)")
# plt.xlabel('x')#etykietka przy osi x
# plt.ylabel('sin(x)')#etykieta przy osi y
# plt.title('Wykres sin(x)')#tytul glowny
# plt.legend()#wyswietla legende
# plt.grid()#siatke dodajeE
# plt.show()#wyswitla wkres

# #WYKRES 6
# #wykres punktowy
# # Tworzenie słownika z danymi
# data={'a':np.arange(50),# tworzy tablicę wartości od 0 do 49 (50 elementów)
#       'c':np.random.randint(0,50,50),# tworzy tablicę 50 losowych liczb całkowitych z przedziału 0-49
#       'd':np.random.rand(50)}# tworzy tablicę 50 losowych liczb z przedziału 0-1
# # Dodanie nowego klucza 'b', który jest sumą 'a' i
# # 10 razy losowych liczb normalnie rozłożonych
# data['b']=data['a']+10*np.random.randn(50)
# # Zastąpienie wartości w kluczu 'd' wartościami bezwzględnymi przemnożonymi przez 100
# data['d']=np.abs(data['d'])*100
# # Wypisanie pierwszych wartości z każdej kolumny w słowniku data
# print(f"a={data['a'][0]},b={data['b'][0]},c={data['c'][0]},d={data['d'][0]}")
# plt.scatter('a','b',# oś x to wartości z kolumny 'a', oś y to wartości z kolumny 'b'
#             c='c',# kolor punktów bazuje na wartościach z kolumny 'c'
# #'c' reprezentuje kolory punktów na wykresie. Każda wartość z
# # kolumny 'c' zostanie przekonwertowana na odpowiedni kolor
# # na wykresie.
#             cmap='magma', # użycie koloru z mapy kolorów 'magma'(kolory kropek z tej mapy)
# #Na przykład, używając cmap='magma', każda wartość liczbowa z
#             # kolumny 'c' zostanie przekonwertowana na kolor
#             # zdefiniowany przez mapę kolorów 'magma'. Ta mapa
#             # kolorów przyporządkowuje niższe wartości do
#             # ciemniejszych kolorów i wyższe wartości do
#             # jaśniejszych kolorów, co pozwala na wyraźne
#             # wizualizowanie różnic w danych numerycznych.
# #Podsumowując, parametr cmap pozwala na wybór mapy kolorów,
#             # która zostanie zastosowana do interpretacji
#             # wartości liczbowych z kolumny 'c' i ich przekształceni
#             # a na konkretne kolory na wykresie punktowym.
#             s='d', # rozmiar punktów bazuje na wartościach z kolumny 'd'(wielkosc kropek)
#             data=data)# dane do wykresu pochodzą ze słownika data(skad te dane maja byc wziete)
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()
# # służy do tworzenia wykresów punktowych, zwanych wykresami
# # rozrzutu (scatter plots). Ta funkcja pozwala na wyświetlenie
# # punktów danych na płaszczyźnie, gdzie każdy punkt ma swoje
# # własne współrzędne x i y.

# #WYKRES 7
# x1=np.arange(0,2,0.02)# generuje sekwencję liczb od 0 do 2 (bez 2) z krokiem 0.02
# x2=np.arange(0,2,0.02)#to co wyzej (czyli dl osi xó dal cos i sin)
# y1=np.sin(2*np.pi*x1) #oblicza wartości sinusoidy dla każdej wartości w tablicy x1
# y2=np.cos(2*np.pi*x2)#oblicza wartości cosinusoidy dla każdej wartości w tablicy x2
# #subplot jest odpowiedzialny za to ze wykresy nie beda nalozone na siebie
# #tylko bedą w (dwoch wierszach,jednej kolumnie,i odnosimy sieponizej do 1 wykrsu)
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'-')#tworzy wykres z x1 i y2 linia cigla
# plt.title('wykres sin(x)')#podpisuje go jako
# #podpisuje osie
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# #wybieramy drugi wykres
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'r-')#linia cigla czerowona
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# #służy do dostosowania odstępów między subplotami w siatce wykresu.
# plt.subplots_adjust(hspace=0.5,#Odstęp pionowy między subplotami(wykresami), gdzie wartość 0.5 oznacza, że odstęp będzie wynosił 0.5
#                     left=0.3,#Wartość z zakresu od 0 do 1, określająca odległość od lewej krawędzi obszaru wykresu
#                     right=0.9,#Wartość z zakresu od 0 do 1, określająca odległość
#                     # od prawej krawędzi obszaru wykresu. Wartość 0.9 oznacza,
#                     # że prawa krawędź subplotów będzie oddalona o 10% szerokości obszaru wykresu od
#                     # prawej krawędzi
#                     top=0.9,#oddalnie od gornej krawedzi
#                     bottom=0.1)#oddalnie od dolenj krawedzi
# #im mniejszy ulamek bilzszy 0 tym wieksze oddalnie
# #im blizszy do 1 tym mniejsze oddalnie
# plt.show()


# #WYKRES 8
# x1=np.arange(0,2,0.02)#generuje osie x
# x2=np.arange(0,2,0.02)
# #Wartości są mnożone przez 2pi w celu przekształcenia argumentu funkcji
# # sinus i cosinus, które są podawane w radianach. W przypadku funkcji sinus
# # i cosinus, pełny okres funkcji wynosi 2π.
# y1=np.sin(2*np.pi*x1)#generuje wartosci sinusidy dla konkrenych xów
# y2=np.cos(2*np.pi*x2)#to samo tylko dl cosinusoidy
# #Tworzysz tę planszę. fig to cała plansza, a axs to podział na poszczególne
# # obszary, gdzie można narysować wykresy. Każdy obszar w axs odpowiada jednemu
# # wykresowi. Więc jeśli zechcesz narysować coś w pierwszym rzędzie, pierwszej
# # kolumnie, będziesz korzystać z axs[0,0], bo indeksy zaczynają się od 0.
# fig, axs = plt.subplots(3,2)
# #obrabianie wykresu w 1 kolumnie i 1 wierszy
# axs[0,0].plot(x1,y1,'-')
# axs[0,0].set_title('wykres sin(x)')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# #obrabianie wykresu w drugim wierszu i 2 kolumnie
# axs[1,1].plot(x2,y2,'r-')
# axs[1,1].set_title('wykres cos(x)')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# #obrabianie wykresu w 3cim wierszu i 1 kolumnie
# axs[2,0].plot(x2,y2,'r-')
# axs[2,0].set_title('wykres cos(x)')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('cos(x)')
# #ponizsze linie sprawiaja ze puste wykresy z obrazka zostaja usuniete
# #(bo sa tam puste sieatki gdy tego nie ma)
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.subplots_adjust(hspace=0.5,#odstep pionowy miedzy wykresami
#                     wspace=0.5)#odstep poziomy miedzy wykrezami
# plt.show()

# #WYKRES 9
# #wykres slupkowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia','Polska'],
#         'Stolica': ['Bruksela' , 'New Delphi', 'Braslia','Warszawa'],
#         'Kontynent':['Europa','Azja','Ameryka Poludniowa','Europa'],
#         'Populacja' : [191129123, 1232132133, 23123123,3867546]}
# df = pd.DataFrame(data)#tworzy data frema ze slownika
# print(df)
# #grupuje na 3 grupy europax2,azja,ameryka zaby potem na tym dziać
# grupa = df.groupby('Kontynent')
# etykiety=np.array(list(grupa.groups.keys()))
#                         #grupa.groups.keys() jest odpowiedzialne za
#                         #wybranie kluczy juz z pogrupowania czyli
#                         #europa,azja,ameryka
#                 #zmienia klucze w liste
#         #ta liste w tablice numpy
# wartosci=list(grupa.agg('Populacja').sum())
# #sumuje wartosci w kolumnie populacja ,troche tak jakby bylo:
# #       europa  azja    ameryka
# #       1       2       2
# #       3       -       -
# #     +________________________
# #       4       2       2
#
# # przygotowuje obiekt figury oraz osi, których możemy użyć do
# # rysowania wykresów i manipulowania ich wyglądem.
# fig,ax = plt.subplots()#pusty nawias-domyslnie jeden wykres
#
# #ax.bar()do rysowania słupkowego wykresu na danej osi ax
# ax.bar(x=etykiety,height=wartosci,color=['yellow','green','red'])
#         #x=etykiety: Określa wartości na osi X, czyli etykiety dla każdego słupka
#                 #height=wartosci: Określa wysokość każdego słupka,
#                 # co odpowiada wartościom dla każdej etykiety
# ax.set_xlabel('Kontynent')
# ax.set_ylabel('Populacja w mld')
#
# #wyswitla liczby populacja po boku etykiety,jej wartoaci
# ax.ticklabel_format(axis='y', style='plain')
# #style='plain': Określa, że chcemy użyć prostego formatu dla etykiet.
# # Format ten pozwala na wyświetlanie liczb bez notacji naukowej
# # (np. 1e6 zamiast 1000000)dla osi y.
# fig.subplots_adjust(left=0.2)
# plt.show()

#WYKRES 10
#wykres kolkowy
df=pd.read_csv('dane.csv',header=0,sep=";",decimal=".")
print(df)
# Grupowanie danych według kolumny 'Imię i nazwisko',
# sumowanie wartości z kolumny 'Wartość zamówienia'.
# Wynikowa seria zawiera sumy wartości zamówień dla każdego unikalnego sprzedawcy.
seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges,texts,autotexts=plt.pie(
                        #tworzy wykres kołowy
                        x=seria,#określa wartości do wyświetlenia na wykresie
                        labels=seria.index,#określa etykiety dla każdego kawałka wykresu,
                        autopct=lambda pct:"{:.1f}%".#określa format wyświetlania procentów na kawałkach
                        format(pct),
                        textprops=dict(color="black"),#określa kolor tekstu na czarny,
                        colors=['red','green'])
plt.title("Suma zamównień dla sprzedawców")
plt.legend(loc='lower right')# Dodanie legendy do wykresu w prawym dolnym rogu.
plt.ylabel('Procentowy wynik wartosci zamówienia')
plt.show()
#wedges: Jest to lista zawierająca obiekty tarczy (wedges) na wykresie kołowym.
# Każdy element listy wedges reprezentuje jeden kawałek wykresu kołowego.
# Te obiekty mogą być modyfikowane, na przykład zmieniając ich kolor, szerokość
# tp.

#texts: Jest to lista zawierająca obiekty tekstu, które są etykietami dla każdego
# kawałka wykresu kołowego. Każdy element listy texts reprezentuje etykietę dla
# jednego kawałka.

#autotexts: Jest to lista zawierająca obiekty tekstu automatycznych etykiet,
# które wyświetlają procentowy udział każdego kawałka na wykresie kołowym.
# Każdy element listy autotexts reprezentuje automatyczną etykietę dla jednego
# kawałka.

