#1 litera - 3 piksele
# DARDANEL - obrazek jakikolwiek, musi być ZAPISANY np. w .png - żeby nie było strat danych
import numpy as np
import cv2


def changeBit(RGB1, kanal, zmienNa):  # przetestowane!

    if kanal != 0 and kanal != 1 and kanal != 2:
        print("Podano zły kanał RGB!!!")
    if zmienNa != 0 and zmienNa != 1:
        print("Podano błędny nowy stan bitu!!!")

    if zmienNa == 0:
        if (RGB1[kanal] % 2) == 1:
            RGB1[kanal] -= 1
    elif zmienNa == 1:
        if (RGB1[kanal] % 2) == 0:
            RGB1[kanal] += 1


img = cv2.imread('DARDANEL.jpg')  # wczytaj z folderu tego projektu - wczyta w skali szaroœci
cv2.imshow('DARDANEL1', img)  # wyowietl, brak .jpg przy nazwie obrazka
print(img[0][2])
print()


wiadomosc = input("Podaj swoją wiadomość: ")

wysokoscObrazu, szerokoscObrazu = img.shape[:2]

print("Długość wiadomości: "+str(len(wiadomosc)))
print("Wymiary wczytanego obrazu: "+str(wysokoscObrazu)+" "+str(szerokoscObrazu))


if (len(wiadomosc)*3+3) > (wysokoscObrazu*szerokoscObrazu):
    print("Obraz jest zbyt mały, aby pomieścić tak dużą wiadomość!")



else:
    for x in range(len(wiadomosc)+1):  # dla każdgo znaku x
        if x != len(wiadomosc):
            szyfrowanyZnak = str(bin(int(ord(wiadomosc[x]))))
            szyfrowanyZnak = szyfrowanyZnak[2:len(szyfrowanyZnak)]
            while len(szyfrowanyZnak) < 9:
                szyfrowanyZnak = "0" + szyfrowanyZnak
        else:
            szyfrowanyZnak = "111111111"

        print()
        print(szyfrowanyZnak)

        for y in range(3):  # dla każdego jego piksela y

            RGB1 = img[int((x*3+y)/szerokoscObrazu), int((x*3+y)%szerokoscObrazu)]  # zaokrągla w dół - dobrze   #%działa jak należy - dobrze   #wczytuje piksel zależny od y - dobrze

            for z in range(3):  # dla każdego jego kanału Z

                # dlugosc=len(str(bin(int(ord(wiadomosc[4])))))-2
                # print("dlugosc: "+str(dlugosc))

                if szyfrowanyZnak[y * 3 + z] == "1":
                    changeBit(RGB1, z, 1)
                elif szyfrowanyZnak[y * 3 + z] == "0":
                    changeBit(RGB1, z, 0)
            print(RGB1)
            img[int((x * 3 + y) / szerokoscObrazu), int((x * 3 + y) % szerokoscObrazu)] = RGB1


# print()
# print("Porównanie piksela w zmienionym i nowo utworzonym obrazie (powinny być identyczne):")
# print(img[0][2])  # działa!

cv2.imshow('DARDANEL2', img)  # wyowietl, brak .jpg przy nazwie obrazka
cv2.imwrite('WYNIK_Stegano.png', img)
img2 = cv2.imread('WYNIK_Stegano.png') # wczytaj z folderu tego projektu - wczyta w skali szaroœci
# print(img2[0][2])


print("\n\n")
wiadomosc2 = ""

for x in range(int(szerokoscObrazu*wysokoscObrazu/3)):  # dla każdych 3 pikseli
    znak = ""
    for y in range(3):  # dla każdego z nich
        for z in range(3):  # dla każdego kanału piksela
            if img2[int((x*3+y)/szerokoscObrazu)][int((x*3+y) % szerokoscObrazu)][z] % 2 == 1:
                znak += "1"
            elif img2[int((x * 3 + y) / szerokoscObrazu)][int((x * 3 + y) % szerokoscObrazu)][z] % 2 == 0:
                znak += "0"
            else:
                print("Obraz zaszyfrowany zawiera błędne bity!!!")

    if znak == "111111111":
        break
    print(znak)
    znakDec = 0
    for f in range(len(znak)):
        if znak[len(znak)-f-1] == "1":
            znakDec += 2**f  # potęgowanie
    print(str(chr(znakDec)))
    wiadomosc2 += str(chr(znakDec))


print("\nTwoja wiadomosc: "+wiadomosc)
print("Twoja odszyfrowana wiadomość: "+wiadomosc2)


cv2.waitKey(0)
