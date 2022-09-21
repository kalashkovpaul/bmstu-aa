import matplotlib.pyplot as plt

from utils import getProcessTime
from algorithms import *
from constants import TO_MILISECONDS, EVEN, ODD

def testAlgorithms() -> None:
    sizeType = int(input("\nТестировать на: 1 - нечетных размерах матриц, 2 - четных: "))
    if ((sizeType > 2) or (sizeType < 1)):
        print("Ошибка: Неверно выбрана опция заполнения матриц")
        return

    evenSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    oddSizes = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]

    timeStdAlg = []
    timeWinAlg = []
    timeOptWinAlg = []

    testSize = evenSizes
    graphText = "\nЧетные размеры матриц"

    if (sizeType == EVEN):
        testSize = evenSizes
        graphText = "\nЧетные размеры матриц"
    elif (sizeType == ODD):
        testSize = oddSizes
        graphText = "\nНечетные размеры матриц"

    print()

    for num in testSize:

        print("Progress:\t", num, " len")

        timeStdAlg.append(getProcessTime(stdAlg, num))
        timeWinAlg.append(getProcessTime(winAlg, num))
        timeOptWinAlg.append(getProcessTime(optWinAlg, num))

    print("\n\nЗамер времени для алгоритмов: \n")

    ind = 0

    for num in testSize:
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" %(num, \
            timeStdAlg[ind] * TO_MILISECONDS, \
            timeWinAlg[ind] * TO_MILISECONDS, \
            timeOptWinAlg[ind] * TO_MILISECONDS))

        ind += 1

    # Graph


    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(testSize, timeWinAlg, label = "Стандартный алгоритм")
    plot.plot(testSize, timeStdAlg, label="Алгоритм Винограда")
    plot.plot(testSize, timeOptWinAlg, label="Оптимизированный алгоритм Винограда")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики" + graphText)
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер")

    plt.show()