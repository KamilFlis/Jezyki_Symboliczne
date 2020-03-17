import math
import random
import time


def exercise_1():
    def is_prime(number):
        if number is 1:
            return "complex"

        if number % 2 is 0:
            return "complex"

        end_condition = int(math.sqrt(number)) + 1

        for i in range(3, end_condition, 2):
            if number % i is 0:
                return "complex"
        else:
            return "prime"

    def mersenne_number(number) -> float:
        return 2 ** number - 1

    for i in range(1, 32):
        mersenne = mersenne_number(i)
        print(mersenne, "is " + is_prime(mersenne))


def exercise_2():
    def printCenter(text, width=80):
        print(text.center(width))

    printCenter("Zażółć gęślą jaźń")
    printCenter("Zażółć gęślą jaźń", 70)


def exercise_3():
    def printFx(fx, x_start=-1, x_stop=1, number_of_intervals=10):
        intervals = ((x_stop - x_start) / number_of_intervals)
        for x in range(x_start * 10, x_stop * 10 + 1, int(10 * intervals)):
            x /= 10
            print(x, "-->", fx(x))

    printFx(lambda a: math.sin(a))


def exercise_4():
    def k4():
        return random.randint(1, 4)

    def k8():
        return random.randint(1, 8)

    def k10():
        return random.randint(1, 10)

    def k20():
        return random.randint(1, 20)

    def getDice(text):
        if text == "k4":
            return k4()
        elif text == "k8":
            return k8()
        elif text == "k10":
            return k10()
        elif text == "k20":
            return k20()
        else:
            return 0

    def rollDice(text):
        numbers = text.split("k")
        fun = "k" + numbers[1]
        sum = 0
        if numbers[0].__contains__("e"):
            numb = numbers[0].split("e")
            number = int(numb[0]) * 10 ** int(numb[1])
        else:
            number = int(numbers[0])

        for times in range(0, number):
            sum += getDice(fun)

        return sum

    print("1k4 -->", rollDice("1k4"))
    print("2k10 -->", rollDice("2k10"))
    print("4k8 -->", rollDice("4k8"))
    print("10k4 -->", rollDice("10k4"))
    print("100k4 -->", rollDice("100k4"))
    print("1k7 -->", rollDice("1k7"))
    print("0k4 -->", rollDice("0k4"))
    print("1e5k4 -->", rollDice("1e5k4"))


def exercise_5():
    def credits(*args, **keywords):
        '''
        Funkcja przyjmuje argumenty zwykle "args" oraz kluczowe "keywords"
        Funkcja wypisuje co sekunde tekst zawarty w argumentach.
        Najpierw argumenty zwykle.
        Potem argumenty kluczowe.
        '''

        for string in args:
            print(string.center(100))
            time.sleep(1)

        for key in keywords:
            print((key + ": " + keywords.get(key)).center(100))
            time.sleep(1)

    credits("Cudowniejszy program pokazowy",
            "Powrot Zlego Markiza Cul-de-Sac",
            Scenariusz="Autor",
            Scenografia="Autor",
            Podziekowania="Python")


if __name__ == "__main__":
    print("Zadanie 1")
    exercise_1()
    print("\nZadanie 2")
    exercise_2()
    print("\nZadanie 3")
    exercise_3()
    print("\nZadanie 4")
    exercise_4()
    print("\nZadanie 5")
    exercise_5()