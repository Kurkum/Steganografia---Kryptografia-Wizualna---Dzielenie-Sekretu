# 124  # modulo p nie robi w przypadku tych przedostatnich czynników
import numpy as np
import cv2
import random


s = int(input("Podaj swoją wiadomość (minimum 100): "))  # nasza sekretna liczba, minimum 100 bo -> patrz nieco
# prymitywny zakres random 3 linie poniżej
n = 4  # ile ma być części
t = 3  # ile części ma wystarczyć do jego odtworzenia
p = random.randint(s + 100, s * 2)
print("P = " + str(p))


# p=1523  # Na potrzeby testów parametry identyczne jak w przykładzie WŁĄCZ


tablicaA = []
for x in range(t - 1):
    tablicaA.append(random.randint(0, s - 1))  # taki wymyśliłem zakres, nie jest z wykładu wzięty ani znikąd!


# tablicaA[0] = 352  # Na potrzeby testów parametry identyczne jak w przykładzie WŁĄCZ
# tablicaA[1] = 62  # Na potrzeby testów parametry identyczne jak w przykładzie WŁĄCZ


wielomian1 = []
for x in range(len(tablicaA)):
    wielomian1.append(tablicaA[len(tablicaA) - 1 - x])
wielomian1.append(s)


print("Tablica liczb losowych 'a': " + str(tablicaA))
print("wielomian1: " + str(wielomian1))


tablicaS = []

for x in range(n):
    newS = 0
    for y in range(len(wielomian1)):
        newS += (wielomian1[y] * ((x+1)**(len(wielomian1) - 1 - y)))

    newS = newS % p
    tablicaS.append(newS)

print("tablicaS: " + str(tablicaS))


# Łączenie sekretu # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

wykorzystywaneKlucze = []

for x in range(t):  # tu nie len(tablicaS) bo potrzebujemy tylko paru kluczy, a nie wszystkich
    ktory = int(input("Podaj klucze, których chcesz użyć [od 1 do " + str(len(tablicaS)) + "]: "))
    newTab = []
    newTab.append(ktory)  # to ma byc numer od 1 liczony, jako że jedziemy od drugiego to pierwszy będzie równy 2
    newTab.append(tablicaS[ktory - 1])
    wykorzystywaneKlucze.append(newTab)

print("\nWykorzystywaneKlucze: " + str(wykorzystywaneKlucze))


X = []
for x in range(len(wykorzystywaneKlucze)):  # ok
    X.append(wykorzystywaneKlucze[x][0])
# print("X: " + str(X))  # linia pomagająca w sprawdzaniu poprawności
Y = []
for x in range(len(wykorzystywaneKlucze)):
    Y.append(wykorzystywaneKlucze[x][1])
# print("Y: " + str(Y))  # linia pomagająca w sprawdzaniu poprawności


tablicaCzynnikow1 = []
for x in range(len(wykorzystywaneKlucze)):  # numer klucza

    # wykonaj 1 czynnik wyniku
    gora = 1
    dol = 1
    for y in range(len(wielomian1)):  # numer nawiasu - tu: 0-3 <- dla 2nawiasowych - dobrze!
        if y != x:
            gora = gora * (-X[y])
            # print(gora)
            dol = dol * (X[x]-X[y])
            # print(dol)

    newCzyn = 0.0
    newCzyn = (int(((gora/dol) * Y[x])) % p)

    tablicaCzynnikow1.append(newCzyn)


print("\nPoszczególne klucze: " + str(tablicaCzynnikow1))


wynik = 0.0

for x in range(len(tablicaCzynnikow1)):
    wynik += tablicaCzynnikow1[x]

wynik = wynik % p

print("\nWYNIK: " + str(int(wynik)))
