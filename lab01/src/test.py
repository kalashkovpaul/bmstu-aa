import matplotlib.pyplot as plt

from utils import getProcessTime
from algorithms import *
from constants import TO_MILISECONDS

def graphLevAndDamerauLev(timeLev: int) -> None:

    sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, timeLev, label = "Левенштейн")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


def graphDamerauLev(
    timeDamerauLev: list[int], timeDamerauLevRecursive: list[int],
    timeDamerauLevRecursiveCache: list[int]) -> None:

    sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, timeDamerauLev, label = "Дамерау-Левенштейн (матричный)")
    plot.plot(sizes, timeDamerauLevRecursive, label="Дамерау-Левенштейн (рекурсия)")
    plot.plot(sizes, timeDamerauLevRecursiveCache, label="Дамерау-Левенштейн (с кэшем)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()

def graphDamerauLevMatrCache(
    timeDamerauLev: list[int],
    timeDamerauLevRecursiveCache: list[int]) -> None:

    sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, timeDamerauLev, label = "Дамерау-Левенштейн (матричный)")
    plot.plot(sizes, timeDamerauLevRecursiveCache, label="Дамерау-Левенштейн (с кэшем)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


# def graph(time_lev_mat, time_lev_cache):

#     sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]

#     fig = plt.figure(figsize=(10, 7))
#     plot = fig.add_subplot()
#     plot.plot(sizes, time_lev_mat, label = "Левенштейн (матричный)")
#     plot.plot(sizes, time_lev_cache, label="Левенштейн (кеш)")

#     plt.legend()
#     plt.grid()
#     plt.title("Временные характеристики")
#     plt.ylabel("Затраченное время (с)")
#     plt.xlabel("Длина")

#     plt.show()


def testAlgorithms():
    timeLev = []
    timeDamerauLev = []
    timeDamerauLevRecursive = []
    timeDamerauLevRecursiveCache = []

    for num in range(10):
        print("Progress:\t", num * 10, "%")
        timeLev.append(getProcessTime(levenshteinDistance, num))
        print("lev is done")
        timeDamerauLev.append(getProcessTime(damerauLevenshteinDistance, num))
        print("domerauLev is done")
        timeDamerauLevRecursive.append(getProcessTime(damerauLevenshteinDistanceRecursive, num))
        print("domerauLev recursive is done")
        timeDamerauLevRecursiveCache.append(getProcessTime(damerauLevenshteinDistanceRecurciveCache, num))
        print("domerauLev recursive with cache is done")

    print("\n\nЗамер времени для алгоритмов: \n")

    ind = 0

    for num in range(10):
        print(" %4d & %.4f & %.4f & %.4f & %.4f \\\\ \n \\hline" %(num, \
            timeLev[ind] * TO_MILISECONDS, \
            timeDamerauLev[ind] * TO_MILISECONDS, \
            timeDamerauLevRecursive[ind] * TO_MILISECONDS, \
            timeDamerauLevRecursiveCache[ind] * TO_MILISECONDS))

        ind += 1

    graphLevAndDamerauLev(timeLev)
    graphDamerauLev(timeDamerauLev, timeDamerauLevRecursive, timeDamerauLevRecursiveCache)
    graphDamerauLevMatrCache(timeDamerauLev, timeDamerauLevRecursiveCache)