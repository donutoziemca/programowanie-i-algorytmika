n = int(input("podaj liczbę naturalną "))
def suma_cyfr(a):
    p = 0
    while a >= 1:
        p += a % 10
        a //= 10
    return p
 
liczba = suma_cyfr(n)
while liczba >= 10:
    liczba = suma_cyfr(liczba)
#if liczba == 3 or liczba == 6 or liczba == 9:
   # print("TAK")
#else:
 #   print("NIE")
print("podana liczba jest podobna do", liczba)
