from constants import EXIT, MSG, PANCAKE, RADIX, BST, TEST
from utils import inputArray
from sorts import pancakeSort, radixSort, bstSort
from test import testSorts
def menu():
    option = -1
    while (option != EXIT):
        try:
            option = int(input(MSG))
        except:
            option = -1
        if (option == PANCAKE):
            arr = inputArray()
            print(pancakeSort(arr, len(arr)))
        elif (option == RADIX):
            arr = inputArray()
            print(radixSort(arr, len(arr)))
        elif (option == BST):
            arr = inputArray()
            print(bstSort(arr, len(arr)))
        elif (option == TEST):
            testSorts()
        elif (option == EXIT):
            print("Спасибо, что пользовались программой :)")
        else:
            "Неверный ввод. Пожалуйста, повторите"
