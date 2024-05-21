import sys
import math

#I metoda
# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("wrong value")
# else:
#     print(result)

# #II metoda
# except Exception:
#     print("Exception")
# else:
#     print


# list1 = [1,2,3,4,5,6,7,8,9]
# list2=[]
# for i in list1:
#     list2.append(pow(i,2))
# print(list2)
#
# list2=[x**2 for x in list1]
# print(list2)
#
# list3=[3**y for y in range(0,6)]
# print(list3)
#
# list4=[x for x in list2 if x%2==1]
# print(list4)
#
# list5=[(x,y)for x in list3 for y in list4]
# print(list5)
#
# list6=[]
# for x in list3:
#     for y in list4:
#         list6.append((x,y))
# print(list6)





# s1={1: 2, 2: 3, 3: 4, 4: 5}
# s2={}
#
# for key,value in s1.items():
#     s2[value]=key
# print(s1)
# print(s2)
#
# s3={v:k for k,v in s2.items()}#to samo co w forze wyzej sie dzieje
# print(s3)


# def rownanie_kwadratowe(a,b,c):
#     delta=b**2-4*a*c
#     if delta<0:
#         print("brak pierwiastkow")
#         return 0
#     elif delta==0:
#         print("jeden pierwiastek")
#         x=(-b+math.sqrt(delta))/(2*a)
#         return x
#     elif delta>0:
#         print("dwa pierwiastki")
#         x1=(-b-math.sqrt(delta))/(2*a)
#         x2=(-b+math.sqrt(delta))/(2*a)
#         return x1,x2
#
# print(rownanie_kwadratowe(6,2,1))
# print(rownanie_kwadratowe(1,2,1))
# print(rownanie_kwadratowe(1,4,2))


# def dlugosc_odcinka(x1=1, x2=1, y1=1, y2=1):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
#
# print(dlugosc_odcinka())                                #wyswietlenie funkcji
# print(dlugosc_odcinka(4, 2, 6, 3))       #podajemy w kolejnsci
# print(dlugosc_odcinka(y2 = 3, x2 = 2, y1 = 3, x1 = 6))  #poza kolejnoscia_1
# print(dlugosc_odcinka(3, 5, y2 = 4, y1 = 3))     #poza kolejnoscia_2


### operacje na plikach
#git config --global user.name "EAWitkiewicz"
#git config --global user.email "161207694+EAWitkiewicz@users.noreply.github.com"