import sys
print("Jedziesz z koksem")

#Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów,
# odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
sporty=["euknkanto","boks szachowy","flanki","podwodny hokej","wyscig strusi","cheese-rolling"]
print(sporty)
sporty.reverse()
print(sporty)
sporty.extend(["kutarate","Quidditch"])
print(sporty)
#chodzi ododanie odtakowego sportu czy o zmiane kolejnosci?



#Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub
# artykułach internetowych. Jako klucz przyjmij skrót danego słowa,
# wartość to rozwinięcie tego skrótu.

#nie beda z gazet
slownik={'kc':"kohcham cie",'pzdr':"pozdro",'cb':"Ciebie",'hwdp':":)",'w8':"wait"}

#Zad 3. Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
gierki={1:"untitled goos game",2:"Counter-Strike",3:"Mario"}

#Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy
# wystąpienia litery a. Użyj funkcji input

#Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie
# wykonasz obliczenia: ab + c. Użyj instrukcji readline() i write()).

#Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich
# jest największa. W zależności od wyniku wyświetl odpowiedni komunikat.
# Użyj zagnieżdżeń.

#Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb
# typu int i float. Następnie za pomocą użycia pętli for podnieś
# każdą liczbę do kwadratu.

#Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# następnie dodaje do listy tylko parzyste liczby.

#Zad. 9.
#Napisz skrypt, który liczy pierwiastek z liczby podanej przez
# użytkownika jeśli użytkownik poda wartość ujemną to powinien
# być wyłapany błąd.