def exercise_1():
    def check_list(list):
        print("Max:", max(list))
        print("Min:", min(list))
        print("Average:", sum(list) / len(list))

    list = [1, 2, 3, 4]
    print("List:", list)
    check_list(list)


def exercise_2():
    def copy_list(list):
        return [x for x in list]

    list = [1, 2, 3, 4]
    print("First list:", list)
    print("Copied list:", copy_list(list))


def exercise_3():
    def average_list(list):
        return [(list[ind] + list[ind - 1] + list[ind + 1]) / 3 if ind != 0 and ind != len(list) - 1
                else list[ind] for ind, x in enumerate(list)]

    list = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", list)
    print("List with averages:", average_list(list))


def exercise_4():
    def list_add(list_1, list_2):
        if len(list_1) <= len(list_2):
            short = len(list_1)
        else:
            short = len(list_2)
        return [list_1[i] + list_2[i] for i in range(0, short)]

    list1 = [1, 2, 3, 3, 8, 1]
    list2 = [2, 1, 3, 3, 6]
    print("List 1:", list1)
    print("List 2:", list2)
    print("List addition:", list_add(list1, list2))


def exercise_5():
    def list_divide(list_1, list_2):
        if len(list_1) <= len(list_2):
            short = len(list_1)
        else:
            short = len(list_2)
        return [list_1[i] if list_2[i] is 0 else list_1[i] / list_2[i] for i in range(0, short)]

    list1 = [3, 1, 0, 5]
    list2 = [8, 0, 1, 3]
    print("List1:", list1)
    print("List2:", list2)
    print("List division:", list_divide(list1, list2))


def exercise_6():
    def take_min_and_max(list):
        list_dec = sorted(list, reverse=True)
        new_list = [list_dec[i] for i in range(0, len(list_dec)) if i not in range(3, len(list_dec) - 3)]
        return [new_list[i] for i in (-3, -2, -1, 0, 1, 2)]

    list = [0, 1, -5, 8, 14, 9, 6]
    print("Original list:", list)
    print("Sorted list:", take_min_and_max(list))


def exercise_7():
    def delete_elements(list):
        for i in range(len(list) - 1, 0, -1):
            if list[i] < 0 or (i + 1) % 3 is 0:
                del list[i]
        return list

    list = [0, 1, 5, 8, 14, 9, 6, -3, -10, 2, 3, 8, 1, -2, 3, -15, 2]
    print("Original list:", list)
    print("New list:", delete_elements(list))

#tu skonczylem
def exercise_8():
    def insert(list, space):
        new_list = [x for x in list]
        for i in range(space, len(list) + space, space + 1):
            new_list.insert(i, 0)

        return new_list

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list:", list)
    print("New list: space = " + str(2), insert(list, 2))
    print("New list: space = " + str(3), insert(list, 3))


def exercise_9():
    def checkboard(size):
        return [[1 if j % 2 is 0 else 0 for j in range(size)] for i in range(size)]

    print(checkboard(4))
    print(checkboard(3))


def exercise_9000():
    def vowels(text):
        vowels_num = 0
        for sign in text:
            if sign.casefold() in "aiueoy":
                vowels_num += 1

        return vowels_num

    def even_vowels_in(texts):
        return [text for text in texts if vowels(text) % 2 is 0]

    print(even_vowels_in(["Robot", "Mech", "Metal Gear", "Android"]))

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
print("\nZadanie 8")
exercise_8()
print("\nZadanie 9")
exercise_9()
print("\nZadanie 9000")
exercise_9000()
