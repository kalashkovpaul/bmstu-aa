from random import randint
from time import process_time
from constants import TIMES

Matrix = [[int]]

def inputMatrix() -> Matrix:
    try:
        row = int(input("\nВведите количество строк: "))
        col = int(input("Введите количество столбцов: "))
        if ((row < 1) or (col < 1)):
            print("Ошибка: Должно быть больше 1")
            return []
    except:
        print("Ошибка: Введено не число")
        return []

    print("\nВведите матрицу построчно (в одной строке - все числа для данной строки матрицы): ")
    matrix = []
    for _ in range(row):
        tmp_arr = list(int(i) for i in input().split())
        if (len(tmp_arr) != col):
            print("Ошибка: Количество чисел не соответствует количеству столбцов матрицы")
            return []
        matrix.append(tmp_arr)
    return matrix

def inputData() -> list(Matrix):
    matA = inputMatrix()
    matB = inputMatrix()
    return matA, matB

def outputMatrix(matrix: Matrix, message: str) -> None:
    print(message)
    row = len(matrix)
    if not row: return
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            print("%-3d" %(matrix[i][j]), end = '')
        print()

def getRandomMatrix(size: int) -> Matrix:
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = randint(0, 50)

    return matrix

def getProcessTime(func: object, size: int) -> float:

    time_res = 0

    for _ in range(TIMES):
        matA = getRandomMatrix(size)
        matB = getRandomMatrix(size)

        time_start = process_time()
        func(matA, matB)
        time_end = process_time()

        time_res += (time_end - time_start)


    return time_res / TIMES