n=int(input("podaj liczbę "))
a=int
def czy_pierwsza(a):
    ls = []
    for x in range(1,a+1):
        if a % x == 0:
            ls.append(x)
    return bool(len(ls) == 2)     
dzielniki = []
for a in range(1, n):
    if not (n % a):
        dzielniki.append(a)
        
print(dzielniki[-1])
print(dzielniki[1])
rozklad = []
rozklad.append(dzielniki[-1])
print(rozklad)
a = (dzielniki[-1])
print(dzielniki)

while a > 2 : 
    if czy_pierwsza(a):
        rozklad.append(a)
        break
    else:
        a = a/dzielniki[1]
        rozklad.append(a)
    
        
print(rozklad)