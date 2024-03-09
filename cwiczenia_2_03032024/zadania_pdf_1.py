import sys
import math
#Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz
# po dwie zmienne każdego typu a następnie wyświetl
#te zmienne
a=6
b=9
c=2.1
d=3.7
e="Pogrzeb kota"
f="""Tak, sluchalam 
myslovitz jak pisalam
 kod"""
g=complex(111,222)
h=complex(333,444)
l=True
m=False
n=list[1,2,3,4,5,6,7,8,9] #trzeba byy petlami to wypisac
rainbow=list["red","orange","yellow","green","blue","purple"]
p=tuple[(1,2,3,4,5,6,7,8)]
r=tuple[("yes","si","ja","hai","tak")]
zakres1=range(1,5)
zakres2=range(1,15,2)


print("\n",a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n",l,"\n",m,"\n",n,"\n",rainbow,"\n",p,"\n",r,"\n",zakres1,"\n",zakres2,"\n")

#ad2. Stwórz skrypt kalkulator,
#w którym wykorzystać wszystkie podstawowe działania arytmetyczne

liczba_1=input("Podaj liczbe: \n")
operacja=input("Podaj operacje: \n")
liczba_2=input("Podaj druga liczbe \n")
def kalkulator(liczba_1,operacja,liczba_2):
    if operacja=="+":
        print(int(liczba_1)+int(liczba_2))
    if operacja=="-":
        print(int(liczba_1)-int(liczba_2))
    if operacja==":":
        print(int(liczba_1)/int(liczba_2))
    if operacja=="*":
        print(int(liczba_1)*int(liczba_2))

kalkulator(liczba_1,operacja,liczba_2)

#Zad3. Napisz skrypt, w którym
# stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

#nie rozumiem co tu trzeba zrobic.Po prostu pozapisywac zmienna np i=+ ? to by nie
#mialo wiecej sensu w petli?
zmienna_jak_moj_humor=4
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor+=2
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor-=2
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor*=2
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor/=2
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor**=2
print(zmienna_jak_moj_humor)
zmienna_jak_moj_humor%=2
print(zmienna_jak_moj_humor)
print("\n")

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
euler=math.exp(10)
print(euler)
dzialanie2=math.pow(math.log(5 + math.sin(8)**2), 1/6)
print(dzialanie2)
dzialanie3=math.floor(3.55)
print(dzialanie3)
dzialanie4=math.ceil(4.8)
print(dzialanie4)

#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej
#metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody
#capitalize)
imie="ELA"
nazwisko="WITKIEWICZ"

print(imie.capitalize(),nazwisko.capitalize())

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się
#słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba
#użyć metody count)

nienawisc_myslovitz="""I nagle skończy się
To wszystko w co wierzysz
Co kochasz, zasypie śnieg
Dziki uniesie Cię wiatr
Upuści cię nagle uderzysz ufałeś mu tak
Ale Ty nigdy nie poddasz się
Ale Ty nigdy nie poddasz się
Nie wierz nigdy nie
W tych co ciągle udają i ciągle uśmiechają się
Nie wierz nigdy nie
W to niebo które zawsze niebieskie jest
Ale Ty nigdy nie poddasz się
Ale Ty nigdy nie poddasz się
Ale Ty nigdy nie poddasz się
Ale Ty nigdy nie poddasz się"""
ile_razy_sie_nie_poddasz=nienawisc_myslovitz.count("Ale Ty nigdy nie poddasz się")
print(ile_razy_sie_nie_poddasz)

# Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę,
# wykorzystując indeksy.
tekst="Tak, zawsze genialny, Idealny muszę być,I muszę chcieć, super luz i już,Setki bzdur i już to nie ja"
#ostatnia=tekst[57]
ostatnia=tekst[len(tekst)-1]
druga=tekst[1]
print(ostatnia)
print(druga,ostatnia)

#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i
# spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)
print(tekst.split(","))

#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
#czym to sie rozni od 1 zadania? ze z ta szesnastkową jest wiecej zabawy?
string="To nie był film"
zmienna=3.20
szesnastkowa=0xFF
szesnaaastkowanr2="FF"
print(string)
print(zmienna)
print(szesnastkowa)
print(int(szesnaaastkowanr2,16))
print("wypisywanie 1 spsosob\n %s\n%f\n%x\n "%(string,zmienna,szesnastkowa))
print("wypisanie 2 sposob\n {}\n{}\n{}\n".format(string,zmienna,szesnastkowa))
print(f"wypisanie 3 sposob\n {string}\n{zmienna}\n{szesnastkowa}")