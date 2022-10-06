# Libs
from time import process_time
from random import randint
import matplotlib.pyplot as plt
from copy import deepcopy

from sorts import pancakeSort, radixSort, bstSort


# Text
MSG = "Меню \n \
1. Блинная сортировка \n \
2. Поразрядная сортировка \n \
3. Сортировка бинарным деревом \n \
4. Замер времени \n \
0. Выход \n\n \
\
Выбор: \
"

# Define
EXIT = 0
PANCAKE = 1
RADIX = 2
BST = 3
TEST = 4

TIMES = 1000
TO_MILISECONDS = 1000

INPUT_KEYBOARD = 1
INPUT_FILE = 0
INPUT_TYPE = 0

FILE = "arr25.csv"


# Functions

def inputArrayKeyboard():
    data = list()
    numbers = 0
    print("Введите массив поэлементно в одной строке (окончание - Enter): ")
    numbers = input().split()
    for i in range(len(numbers)):
        try:
            data.append(int(numbers[i]))
        except:
            print("Ошибка: введено не число")
            return []
    return data


def inputArrayFile():
    f = open(FILE, "r")
    data = list()
    for line in f:
        try:
            data.append(int(line))
        except:
            print("Ошибка: введено не число")
            return []
    return data


def inputArray():
    if (INPUT_TYPE):
        data = inputArrayKeyboard()
    else:
        data = inputArrayFile()
    return data


def getSortedArray(size):
    arr = list()
    for i in range(size):
        arr.append(i)
    return arr

def getReverseSortedArray(size):
    arr = list()
    for i in range(size):
        arr.append(size - i)
    return arr

def getRandomArray(size):
    arr = list()
    for _ in range(size):
        arr.append(randint(0, 100))
    return arr


def getArray(option, size):
    #size = int(input("Введите количество элементов в массиве: "))
    #option = int(input("Введите тип массива: "))
    type = "Не определено"
    if (option == 0):
        arr = getSortedArray(size)
        type = "Отсортированный "
    elif (option == 1):
        arr = getReverseSortedArray(size)
        type = "Отсортированный в обратном порядке "
    elif (option == 2):
        arr = getRandomArray(size)
        type = "Случайный "
    return arr, type

def getExactSort():
    option = int(input("Введите номер сортировки: "))
    if (option == 0):
        func = pancakeSort
    elif (option == 1):
        func = radixSort
    elif (option == 2):
        func = bstSort
    return func

def getProcessTime(func, arr):
    resultTime = 0
    for _ in range(TIMES):
        tmpArray = deepcopy(arr)

        timeStart = process_time()
        func(tmpArray, len(tmpArray))
        timeEnd = process_time()

        resultTime += (timeEnd - timeStart)
    return resultTime / TIMES


def testSorts():
    pancakeSortTime = []
    radixSortTime = []
    bstSortTime = []
    option = int(input("\nВведите тип массива \n(0 - отсортированный, 1 - отсортированный в обратном порядке, 2 - случайный): "))
    print("Идёт замер времени, подождите...")
    sizes = [100, 200, 300, 400, 500, 600, 700, 800]

    for num in sizes:
        arr, type = getArray(option, num)
        pancakeSortTime.append(getProcessTime(pancakeSort, arr))
        radixSortTime.append(getProcessTime(radixSort, arr))
        bstSortTime.append(getProcessTime(bstSort, arr))
    print("\n\n" + type + "массив: \n")

    exactSize = 0

    for num in sizes:
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" %(num, \
            pancakeSortTime[exactSize] * TO_MILISECONDS, \
            radixSortTime[exactSize] * TO_MILISECONDS,
            bstSortTime[exactSize] * TO_MILISECONDS))

        exactSize += 1

    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, pancakeSortTime, label = "Блинная сортировка")
    plot.plot(sizes, radixSortTime, label="Поразрядная сортировка")
    plot.plot(sizes, bstSortTime, label="Сортировка бинарным деревом")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов сортировок\n" + type + "массив")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


def main():
    option = -1
    while (option != EXIT):
        try:
            option = int(input(MSG))
        except:
            option = -1
        if (option == PANCAKE):
            arr = inputArray()
            print(pancakeSort(arr, len(arr)))
        elif (option == RADIX):
            arr = inputArray()
            print(radixSort(arr, len(arr)))
        elif (option == BST):
            arr = inputArray()
            print(bstSort(arr, len(arr)))
        elif (option == TEST):
            testSorts()
        elif (option == EXIT):
            print("Спасибо, что пользовались программой :)")
        else:
            "Неверный ввод. Пожалуйста, повторите"

if __name__ == "__main__":
    main()
