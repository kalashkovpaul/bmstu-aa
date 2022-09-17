# Lab 01, Algorithm analysis
# Task: calculate Levenshtein distance - non-recurcive algorithm,
# calculate Damerau-Levenshtein distance - non-recurcive,
# recursive algorithm without cache, with cache

from utils import createLevenshteinMatrix, printMatrix, Matrix

def levenshteinDistance(str1: str, str2: str, output: bool = True) -> int:
    n = len(str1)
    m = len(str2)
    matrix = createLevenshteinMatrix(n + 1, m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            add = matrix[i - 1][j] + 1
            delete = matrix[i][j - 1] + 1
            change = matrix[i - 1][j - 1]

            if (str1[i - 1] != str2[j - 1]):
                change += 1

            matrix[i][j] = min(add, delete, change)

    if (output):
        print("\nМатрица, с помощью которой происходило вычисление расстояния Левенштейна:")
        printMatrix(matrix, str1, str2)

    return matrix[n][m]

def damerauLevenshteinDistance(str1: str, str2: str, output: bool = True) -> int:
    n = len(str1)
    m = len(str2)
    matrix = createLevenshteinMatrix(n + 1, m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            add = matrix[i - 1][j] + 1
            delete = matrix[i][j - 1] + 1
            change = matrix[i - 1][j - 1]
            if (str1[i - 1] != str2[j - 1]):
                change += 1
            swap = n
            if (i > 1 and j > 1 and
                str1[i - 1] == str2[j - 2] and
                str1[i - 2] == str2[j - 1]):
                    swap = matrix[i - 2][j - 2] + 1

            matrix[i][j] = min(add, delete, change, swap)

    if (output):
        print("\nМатрица, с помощью которой происходило вычисление " +
            "расстояния Дамерау-Левенштейна:")
        printMatrix(matrix, str1, str2)

    return matrix[n][m]

def damerauLevenshteinDistanceRecursive(str1: str, str2: str, output: bool = True) -> int:
    n = len(str1)
    m = len(str2)
    flag = 0
    if ((n == 0) or (m == 0)):
        return abs(n - m)

    if (str1[-1] != str2[-1]):
        flag = 1

    minDistance = min(
        damerauLevenshteinDistanceRecursive(str1[:-1], str2) + 1,
        damerauLevenshteinDistanceRecursive(str1, str2[:-1]) + 1,
        damerauLevenshteinDistanceRecursive(str1[:-1], str2[:-1]) + flag
    )
    if (n > 1 and m > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]):
        minDistance = min(
            minDistance,
            damerauLevenshteinDistanceRecursive(str1[:-2], str2[:-2]) + 1
        )

    return minDistance

def recursiveWithCache(
    str1: str, str2: str, n: int, m: int, matrix: Matrix) -> None:
    if (matrix[n][m] != -1):
        return matrix[n][m]
    if (n == 0):
        matrix[n][m] = m
        return matrix[n][m]
    if ((n > 0) and (m == 0)):
        matrix[n][m] = n
        return matrix[n][m]

    add = recursiveWithCache(str1, str2, n - 1, m, matrix) + 1
    delete = recursiveWithCache(str1, str2, n, m - 1, matrix) + 1
    change = recursiveWithCache(str1, str2, n - 1, m - 1, matrix)
    if (str1[n - 1] != str2[m - 1]):
        change += 1 # flag

    matrix[n][m] = min(add, delete, change)
    if (n > 1 and m > 1 and
        str1[n - 1] == str2[m - 2] and
        str1[n - 2] == str2[m - 1]):

        matrix[n][m] = min(
            matrix[n][m],
            recursiveWithCache(str1, str2, n - 2, m - 2, matrix) + 1
        )

    return matrix[n][m]

def damerauLevenshteinDistanceRecurciveCache(
    str1: str, str2: str, output: bool = True) -> int:
    n = len(str1)
    m = len(str2)
    matrix = createLevenshteinMatrix(n + 1, m + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j] = -1

    recursiveWithCache(str1, str2, n, m, matrix)

    if (output):
        print("\nМатрица для кеша рекурсивного нахождения расстояния Дамерау-Левенштейна:")
        printMatrix(matrix, str1, str2)

    return matrix[n][m]
