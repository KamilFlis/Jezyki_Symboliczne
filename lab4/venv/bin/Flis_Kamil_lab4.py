import math
import random

def exercise_1():
    def sin_cos(x):
        return math.sin(x), math.cos(x)

    # 1 stopien = pi/180
    for i in range(11):
        y = sin_cos(9 * i * math.pi / 180)
        print("Kat: " + str(i * 9) +  "; sin: " + str(y[0]) + "; cos: " + str(y[1]))


def exercise_2():
    def two_args(x, y):
        return y, x + y

    def fibonacci(n):
        x = 0, 1
        for i in range(n - 1):
            x = two_args(x[0], x[1])
            print(*x, sep=" ", end=" ")
        return x[1]

    n = 7
    print("\nFibonacci (" + str(n) + ") = " + str(fibonacci(n)))


def exercise_3():
    def blur(list_to_be_blurred, weight):
        return [(list_to_be_blurred[i - 1] * weight[0] + element * weight[1] + list_to_be_blurred[i + 1] * weight[2]) / sum(weight) if i is not 0
                    and i is not len(list_to_be_blurred) - 1 else element for i, element in enumerate(list_to_be_blurred)]

    list_of_20 = [random.randrange(0, 15) for x in range(20)]
    blurred_list = blur(list_of_20, (2, 3, 1))
    print("Original list:", list_of_20)
    print("Blurred list:", blurred_list)


def exercise_4():
    def name_mark_sort_by_name(dictionary):
        for name in sorted(dictionary.keys()):
            print(name)

    def name_mark_print(dictionary):
        for key, value in dictionary.items():
            print(key, value)

    name_mark_dict = {"Mathew": 3, "Anne": 5, "John": 4, "Kate": 3}
    name_mark_sort_by_name(name_mark_dict)
    name_mark_print(name_mark_dict)


def exercise_5():
    def average(dictionary):
        for person_name, person_value in dictionary.items():
            sum = 0
            for mark in person_value.values():
                sum += mark

            avg = sum / len(person_value.values())
            if avg < 3:
                print(person_name, avg)

    def average_category(dictionary):
        sums = {key: 0 for name, marks in dictionary.items() for key in marks.keys()}
        elements_number = sums.copy()

        for marks in dictionary.values():
            for category, mark in marks.items():
                sums[category] += mark
                elements_number[category] += 1

        for category, sum in sums.items():
            avg = sum / elements_number.get(category)
            print(category, avg)

    name_category_mark = {"Mathew":{"python_1": 4, "kolokwium": 3, "odpowiedz ustna": 2},
                          "Anne": {"python_1": 3, "kolokwium": 5, "odpowiedz ustna": 4},
                          "Ethan": {"python_1": 2, "odpowiedz ustna": 3}}

    average(name_category_mark)
    average_category(name_category_mark)


def exercise_6():
    def sleep_length(dictionary):
        return {key: 8 / math.log10(value) if value in range(200) else "Wieczny odpoczynek" for key, value in dictionary.items() if value > 0}

    dic = {"Mathew": -3, "Anne": 20, "Selena": 2000}
    print("Original dictionary:", dic)
    print("Sleep length dictionary:", sleep_length(dic))


def exercise_7():
    def print_board(board):
        for i in board:
            print(i)

    board = [[False for col in range(10)] for row in range(10)]
    for i in range(21):
        board[random.randint(0, 9)][random.randint(0, 9)] = True

    used_coords = set()
    true_counter = 0

    board_show = [["_" for col in range(10)] for row in range(10)]

    print("Gra w statki!")
    print("Traf 20 statkow, zeby wygrac")
    print("X - trafiony")
    print("Y - pudlo")

    while true_counter != 20:
        print_board(board_show)
        xy = input("Podaj x, y [-10, 10): ")
        xy = xy.split(" ")
        coords = (int(xy[0]), int(xy[1]))
        if -10 <= coords[0] < 10 and -10 <= coords[1] < 10:
            if coords not in used_coords:
                used_coords.add(coords)
                if board[coords[0]][coords[1]] is True:
                    print("Trafiony!")
                    board_show[coords[0]][coords[1]] = "X"
                    true_counter += 1
                else:
                    board_show[coords[0]][coords[1]] = "Y"
                    print("Pudlo!")
            else:
                print("Juz tam strzelano")
        else:
            print("Wybierz wspolrzedne w przedziale [0, 10)")
            continue

    print("Wygrales!")


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
print("\nZadanie 6")
exercise_6()
print("\nZadanie 7")
exercise_7()