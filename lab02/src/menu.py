from constants import EXIT, MESSAGE, ALL_ALG, STD_ALG, WIN_ALG, OPT_WIN_ALG, TEST
from utils import inputData, outputMatrix
from algorithms import *
from test import testAlgorithms

def menu():
    option = -1

    while (option != EXIT):
        try:
            option = int(input(MESSAGE))
        except:
            option = -1

        if (option == STD_ALG):
            matA, matB = inputData()
            outputMatrix(stdAlg(matA, matB), "Результат: ")
        elif (option == WIN_ALG):
            matA, matB = inputData()
            outputMatrix(winAlg(matA, matB), "Результат: ")
        elif (option == OPT_WIN_ALG):
            matA, matB = inputData()
            outputMatrix(optWinAlg(matA, matB), "Результат: ")
        elif (option == ALL_ALG):
            matA, matB = inputData()
            outputMatrix(stdAlg(matA, matB), "Результат работы стандартного алгоритма: ")
            outputMatrix(winAlg(matA, matB), "Результат работы алгоритма Винограда: ")
            outputMatrix(optWinAlg(matA, matB), "Результат работы оптимизированного алгоритма Винограда: ")
        elif (option == TEST):
            testAlgorithms()
        elif (option == EXIT):
            print("Спасибо, что пользовались этой программой :)")
        else:
            print("\nПовторите ввод\n")