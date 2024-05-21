
#przeniesc plik na nazwe projektu
# plik = open('tekst.txt', 'r', encoding='utf-8') #encoding - polskie znaki, r - czytanie
# znaki = plik.read(10) #wczyta 10 znakow
#
# linia = plik.readline() #odczyta cala linijke
# linie = plik.readlines() #odczyta cala zawartosc
#
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)



# plik=open('tekst1.txt', 'a+') #'w'- 'a+'-odzcytanie zawartosci    'r'-
# plik.write('aaaaaaaa')
# plik.seek(105)
# zanki=plik.read(10)
# plik.close()
# #plik=

# #przeniesc plik na nazwe projektu
# plik = open('tekst.txt', 'r', encoding='utf-8') #encoding - polskie znaki, r - czytanie / w - plik nie musi istniec
# znaki = plik.read(10) #wczyta 10 znakow
#
# linia = plik.readline() #odczyta cala linijke
# linie = plik.readlines() #odczyta cala zawartosc
#
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)

# plik = open('tekst1.txt', 'w', encoding='utf-8')    #doda plik  tekstowy z zawartoscia aaaaaaaaaaaaaaaaaaaa, jesli podalibysmy istniejacy plik t nadpiszemy zawartosc, a+ zamiast w mozena odczytywac i nadpisywac zawartosc
# plik.write('aaaaaaaaaaaa')
# plik.close()


# plik = open('tekst.txt', 'a+')      #w+ zamiast a+ czysci cala zawartosc
# plik.write('aaaaaaaaaaaaaaassscxcxz')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()
# print(znaki)

# with open('tekst.txt', 'r') as f:      #odczytanie zawartosci, roznica jest taka ze nie trzeba zamykac pliku, z automatu sie zamknie
#     lines = f.readlines()
# print(lines)


#nie trzeba pamietac o zamykaniu pliku
# with open('tekst.txt', 'r') as f:
#     lines = f.readlines()
# print(lines)