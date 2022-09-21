from constants import EXIT, MESSAGE, LEV, DAM, DAM_REC, DAM_REC_CACHE, TEST
from utils import getInputStrings
from algorithms import *
from test import testAlgorithms

def menu():
    option = -1

    while (option != EXIT):
        try:
            option = int(input(MESSAGE))
        except:
            option = -1

        if (option == LEV):
            str1, str2 = getInputStrings()
            print("\nРезультат: ", levenshteinDistance(str1, str2))
        elif (option == DAM):
            str1, str2 = getInputStrings()
            print("\nРезультат: ", damerauLevenshteinDistance(str1, str2))

        elif (option == DAM_REC):
            str1, str2 = getInputStrings()
            print("\nРезультат: ", damerauLevenshteinDistanceRecursive(str1, str2))

        elif (option == DAM_REC_CACHE):
            str1, str2 = getInputStrings()
            print("\nРезультат: ", damerauLevenshteinDistanceRecurciveCache(str1, str2))

        elif (option == TEST):
            testAlgorithms()

        elif (option == EXIT):
            print("Спасибо, что пользовались этой программой :)")

        else:
            print("\nПовторите ввод\n")