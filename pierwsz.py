def czy_pierwsza(a):
    ls = []
    for x in range(1,a+1):
        if a % x == 0:
            ls.append(x)
    return (len(ls) == 2)     
print(czy_pierwsza(1))
print(czy_pierwsza(5))
print(czy_pierwsza(12))
print(czy_pierwsza(11))

print(czy_pierwsza(124))
