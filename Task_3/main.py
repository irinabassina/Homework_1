# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# Пример: 10 -> 1 2 4 8

N = int (input("Введите число N: "))
if N<1:
    print('нет решения')
k=1    
while k<=N:
    print(k,end=' ')
    k=k*2