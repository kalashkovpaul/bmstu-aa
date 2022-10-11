# Lab 01, Matrix multiplication
# Task: implement 3 algorithms of matrix multiplication:
# standart algorithm, winograd algorithm, optimized winograd algorithm.
# Optimizations:
# 1. кэшировать of N / 2
# 2. * 2 => << 1
# 3. k += 2

from utils import Matrix


def stdAlg(matA: Matrix, matB: Matrix) -> Matrix:
    if (len(matA[0]) != len(matB)):
        print("Ошибка: Размеры не совпадают - умножение таких матриц невозможно")
        return []

    n = len(matA)
    m = len(matA[0])
    t = len(matB[0])

    result = [[0] * t for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(t):
                result[i][j] += matA[i][k] * matB[k][j]

    return result

def winAlg(matA: Matrix, matB: Matrix) -> Matrix:
    if (len(matA[0]) != len(matB)):
        print("Ошибка: Размеры не совпадают - умножение таких матриц невозможно")
        return []

    n = len(matA)
    m = len(matA[0])
    t = len(matB[0])

    result = [[0] * t for _ in range(n)]

    rowSum = [0] * n
    colSum = [0] * t

    for i in range(n):
        for j in range(0, m // 2):
            rowSum[i] = rowSum[i] + matA[i][2 * j] * matA[i][2 * j + 1]
    for i in range(t):
        for j in range(0, m // 2):
            colSum[i] = colSum[i] + matB[2 * j][i] * matB[2 * j + 1][i]


    for i in range(n):
        for j in range(t):
            result[i][j] = -rowSum[i] - colSum[j]
            for k in range(0, m // 2):
                result[i][j] = result[i][j] + (matA[i][2 * k + 1] + matB[2 * k][j]) * (matA[i][2 * k] + matB[2 * k + 1][j])

    if (m % 2 == 1):
        for i in range(n):
            for j in range(t):
                result[i][j] = result[i][j] + matA[i][m - 1] * matB[m - 1][j]

    return result

def optWinAlg(matA: Matrix, matB: Matrix) -> Matrix:
    if (not len(matA) or len(matA[0]) != len(matB)):
        print("Ошибка: Размеры не совпадают - умножение таких матриц невозможно")
        return []

    n = len(matA)
    m = len(matA[0])
    t = len(matB[0])

    result = [[0] * t for _ in range(n)]

    rowSum = [0] * n
    colSum = [0] * t

    halfM = m // 2

    for i in range(n):
        for j in range(0, halfM):
            rowSum[i] += matA[i][j << 1] * matA[i][(j << 1) + 1]
    for i in range(t):
        for j in range(0, halfM):
            colSum[i] += matB[j << 1][i] * matB[(j << 1) + 1][i]


    for i in range(n):
        for j in range(t):
            result[i][j] = -rowSum[i] - colSum[j]
            for k in range(0, halfM):
                result[i][j] += (matA[i][(k << 1) + 1] + matB[k << 1][j]) * (matA[i][k << 1] + matB[(k << 1) + 1][j])

    if (m % 2 == 1):
        for i in range(n):
            for j in range(t):
                result[i][j] += + matA[i][m - 1] * matB[m - 1][j]

    return result

