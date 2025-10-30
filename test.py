import time

a = float(input("podaj liczbę "))
y = 0
if a >= 0:
    while a >= y:
        y += 1
    print(F"podłoga wynosi {y - 1}")
if a < 0:
    while a < y:
        y -= 1
    print(F"podłoga wynosi {y}")
time.sleep(10)