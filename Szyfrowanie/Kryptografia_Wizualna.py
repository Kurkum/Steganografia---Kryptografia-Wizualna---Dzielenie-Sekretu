# UWAGA! Ten nowy obraz jest duży, pamiętaj że będzie się szyfrować nawet minutę a nie tak jak małe obrazy testowe!
# M - wiadomość, mapa bitowa monochromatyczna, możesz zrobić w paintcie - i w paintcie daj jakiś napis na tym obrazku
# wstawiając tekst lub obraz - tutaj "Astrid"
# MP - to samo, ale całkowicie białe - powiększy się automatycznie
import numpy as np
import random
import cv2


def naCzarno(img1, napis, x, y):  # działa, ify działaja jak trzeba
    if napis[0] == "1" or napis[1] == "1":
        img1[x * 2][y * 2] = 0
    if napis[0] == "2" or napis[1] == "2":
        img1[x * 2][y * 2 + 1] = 0
    if napis[0] == "3" or napis[1] == "3":
        img1[x * 2 + 1][y * 2] = 0
    if napis[0] == "4" or napis[1] == "4":
        img1[x * 2 + 1][y * 2 + 1] = 0


tablica = []
tablica.append("34")
tablica.append("12")
tablica.append("13")
tablica.append("24")
tablica.append("14")
tablica.append("23")
lustro = []
lustro.append("12")
lustro.append("34")
lustro.append("24")
lustro.append("13")
lustro.append("23")
lustro.append("14")


img0 = cv2.imread('M2.bmp', 0)
cv2.imshow('PODANA WIADOMOSC', img0)
# print(img0[0][2])
# działa
wysokoscObrazu, szerokoscObrazu = img0.shape[:2]


img1 = cv2.imread('MP2.bmp', 0)
img1 = cv2.resize(img1, (0, 0), fx=2, fy=2)  # szerokość i wysokość
img2 = cv2.imread('MP2.bmp', 0)
img2 = cv2.resize(img2, (0, 0), fx=2, fy=2)  # szerokość i wysokość

# print(tablica[0])
# img2[0][0]=0
# naCzarno(img2, tablica[0], 0, 0)
# naCzarno(img2, lustro[0], 0, 0)

# print(img1[0][0])  # działa, jest monochromatycznie
# cv2.imshow('MONOPUSTE', img2)  # działa, wyświetla co trzeba
cv2.imwrite('WYNIK.bmp', img2)


for x in range(wysokoscObrazu):
    for y in range(szerokoscObrazu):
        grey = img0[x][y]
        # print(grey)
        los = random.randint(0, 5)
        # print(los)

        if grey == 0:  # piksel oryginalnie jest czarny
            # print("czarny")
            naCzarno(img1, tablica[los], x, y)
            naCzarno(img2, lustro[los], x, y)

        else:  # piksel oryginalnie jest biały
            # print("biały")
            naCzarno(img1, tablica[los], x, y)
            naCzarno(img2, tablica[los], x, y)


cv2.imshow('OBRAZ1', img1)  # one będą w większości identyczne - w wiekszości - we wszystkich białych miejscach
cv2.imshow('OBRAZ2', img2)


img3 = img1
# cv2.imshow('OBRAZ3', img3)
wysokoscObrazu2, szerokoscObrazu2 = img3.shape[:2]

for x in range(wysokoscObrazu2):
    for y in range(szerokoscObrazu2):
        print(img2[x][y])
        if img2[x][y] == 0:  # że czarny, sprawdza tylko img2 bo informacje z img1 już ma -> powyżej jest "img3=img1"
            img3[x][y] = 0


cv2.imshow('WYNIK', img3)
cv2.imwrite('WYNIK_Wizual.bmp', img3)
cv2.waitKey(0)
