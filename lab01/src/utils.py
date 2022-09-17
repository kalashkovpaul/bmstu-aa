import string
from random import choice
from time import process_time
from constants import TIMES

Matrix = [[int]]

def createLevenshteinMatrix(n: int, m: int) -> Matrix:
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        matrix[i][0] = i
    for j in range(m):
        matrix[0][j] = j
    return matrix

def printMatrix(matrix: Matrix, str1: str, str2: str) -> None:
    print("\n   ∅  " + "  ".join([letter for letter in str2]))
    for i in range(len(str1) + 1):
        print(str1[i - 1] if (i != 0) else "∅", end = "")
        for j in range(len(str2) + 1):
            print("  " + str(matrix[i][j]), end = "")
        print("")

def getInputStrings() -> list[str]:
    str1 = input("\nВведите 1-ую строку:\t")
    str2 = input("Введите 2-ую строку:\t")
    return str1, str2

def getRandomString(size: int) -> str:
    letters = string.ascii_lowercase
    return "".join(choice(letters) for _ in range(size))

def getProcessTime(func: object, size: int) -> float:

    time_res = 0

    for _ in range(TIMES):
        str1 = getRandomString(size)
        str2 = getRandomString(size)

        time_start = process_time()
        func(str1, str2, output = False)
        time_end = process_time()

        time_res += (time_end - time_start)


    return time_res / TIMES