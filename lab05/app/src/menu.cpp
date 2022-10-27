#include "menu.h"

void menu() {
    int option = -1;
    while (option != 0) {
        printMenu();
        std::cout << "Выбор: ";
        std::cin >> option;

        if (option == 1) {
            int size = 0, count = 0;
            std::cout << "\nРазмер: ";
            std::cin >> size;
            std::cout << "Количество: ";
            std::cin >> count;

            parseLinear(count, size, true);
        } else if (option == 2) {
            int size = 0, count = 0;
            std::cout << "\nРазмер: ";
            std::cin >> size;
            std::cout << "Количество: ";
            std::cin >> count;

            parseParallel(count, size, true);
        } else if (option == 3) {
            timeMessage();
        }
        else if (option == 4) {
            stagesInfo();
        } else if (option == 0) {
            printf("\nСпасибо, что пользовались данной программой :)");
        } else {
            printf("\nОшибка: Неверно введен пункт меню. Повторите\n");
        }
    }
}