
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

#nie trzeba pamietac o zamykaniu pliku
with open('tekst.txt', 'r') as f:
    lines = f.readlines()
print(lines)