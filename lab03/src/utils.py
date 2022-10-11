from constants import FILE, INPUT_TYPE, TIMES
from sorts import pancakeSort, radixSort, bstSort
from copy import deepcopy
from time import process_time
from random import randint

def inputArrayKeyboard():
    data = list()
    numbers = 0
    print("Введите массив поэлементно в одной строке (окончание - Enter): ")
    numbers = input().split()
    for i in range(len(numbers)):
        try:
            data.append(int(numbers[i]))
            if (numbers[i] < 0):
                raise Exception
        except:
            print("Ошибка: введено не неотрицательное число")
            return []
    return data


def inputArrayFile():
    f = open(FILE, "r")
    data = list()
    for line in f:
        try:
            data.append(int(line))
            if int(line) < 0:
                raise Exception
        except:
            print("Ошибка: введено не неотрицательное число")
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