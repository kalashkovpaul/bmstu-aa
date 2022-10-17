from utils import getArray, getProcessTime
from sorts import pancakeSort, radixSort, bstSort
from constants import TO_MILISECONDS
import matplotlib.pyplot as plt

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
    plot.plot(sizes, radixSortTime, ":", label="Поразрядная сортировка")
    plot.plot(sizes, bstSortTime, "--", label="Сортировка бинарным деревом")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов сортировок\n" + type + "массив")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()