import math
import sys


def exercise_1():
    print("\nZadanie 1")
    print("Operatory ktorych nie ma w C/C++")
    print("Potega")
    power = 2 ** 5
    print("2^5 =", power)

    print("Pierwiastek")
    radical = 4 // 2
    print("4 // 2 =", radical)

    list = [1, 2, 3, 4, 5]
    numIn = 6
    numNotIn = 2

    print("in, not in")
    if numIn in list:
        print(numIn, "jest w liscie")
    else:
        print(numIn, "nie ma w liscie")

    if numNotIn not in list:
        print(numNotIn, "nie ma w liscie")
    else:
        print(numNotIn, "jest w liscie")

    print("is, is not")
    x = 5
    y = 5

    print("is, is not")
    if x is y:
        print(x, "=", y)
    else:
        print(x, "!=", y)

    if x is not y:
        print(x, "!=", y)
    else:
        print(x, "=", y)


def exercise_2():
    def isLeap(year):
        return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

    print("\nZadanie 2")
    print("Wypisuje informacje czy podany rok jest przestepny")
    year = input("Podaj rok: ")
    year = int(year)

    if isLeap(year):
        print("Rok " + str(year) + " jest przestepny")
    else:
        print("Rok " + str(year) + " nie jest przestepny")


def exercise_3():
    def decimal_range(start, stop, increment):
        while start < stop:
            yield start
            start += increment

    print("\nZadanie 3")
    print("Oblicza wartosc sin(x) dla x z przedzialu (-1, 1)")
    print(" \tx \t\tsin(x)")
    for x in decimal_range(-1.0, 1.0, 0.1):
        print("{0:8.2f} {1:+10.6f}".format(x, math.sin(x)))


def exercise_4():
    print("\nZadanie 4")
    print("Sprawdza czy liczba jest zlozona")
    num = 9
    if num % 2 is 0:
        print("Liczba " + str(num) + " jest zlozona")
        return

    stop = math.sqrt(num) + 1

    for x in range(3, int(stop), 2):
        if num % x == 0:
            print("Liczba " + str(num) + " jest zlozona")
            break
    else:
        print("Liczba " + str(num) + " jest pierwsza")

    print("Warunek zakonczenia petli:", int(stop))


def exercise_5():
    def listToString(list):
        text = ""
        for string in list:
            text += string
        return text

    print("\nZadanie 5")
    print("Zamienia wszystkie samogloski na 'a' w tekscie")

    text = input("Podaj tekst: ")
    #text = "Ala ma kota, a Ola ma psa"
    vowels = ['e', 'y', 'o', 'i', 'E', 'Y', 'O', 'I']
    print("Przed: " + text)

    textList = list(text)

    for letter in range(0, len(textList)):
        if textList[letter] in vowels:
            textList[letter] = 'a'

    text = listToString(textList)
    print("Po: " + text)


def exercise_6():
    print("\nZadanie 6")
    print("Wypisuje opinie o podanym dniu tygodnia")

    days = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
    opinion = {
        days[0]: 'slaby',
        days[1]: 'troszczke lepszy niz poniedzialek',
        days[2]: 'spoko',
        days[3]: 'w porzadku',
        days[4]: 'super',
        days[5]: 'super',
        days[6]: 'slaba'
    }

    for i in range(0, 2):
        day = input("Podaj dzien tygodnia ")
        if day.casefold() in days:
            break
        else:
            if i is 1:
                print("Znowu zly dzien tygodnia. Koncze dzialanie...")
                return
            print("Podales zly dzien tygodnia")

    print(day + " jest " + opinion.get(day.casefold()))


#method to choose exercises
def switch(argument):
    switcher = {
        1: exercise_1,
        2: exercise_2,
        3: exercise_3,
        4: exercise_4,
        5: exercise_5,
        6: exercise_6,
    }

    func = switcher.get(argument)
    return func()


if __name__ == '__main__':

    while True:
        try:
            number = input("\nPodar nr zadania (1-6)\nWpisz 0 zeby zakonczyc: ")
            number = int(number)
        except ValueError:
            print("Wpisano tekst")
            continue

        if number is 0:
            print("Koniec")
            sys.exit()

        if number not in range(1, 7):
            print("Zly numer zadania")
            continue

        switch(number)
