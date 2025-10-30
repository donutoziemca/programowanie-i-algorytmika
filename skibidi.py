from math import sqrt, ceil
lista = []
n = int(input("podaj liczbę do sprawdzenia "))
for a in range (1,n+1):
    if n % a == 0:
        lista.append(a)
print(bool(len(lista) == 2))