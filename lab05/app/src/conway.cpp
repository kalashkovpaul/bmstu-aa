#include "conway.h"

double currentTime = 0;

std::vector<double> t1;
std::vector<double> t2;
std::vector<double> t3;

void logLinear(matrix_t &matrix, int task, int stage, \
    void (*func)(matrix_t &), bool needPrinting) {

    std::chrono::time_point<std::chrono::system_clock> startTime, endTime;
    double resultStartTime = currentTime, resultTime = 0;

    startTime = std::chrono::system_clock::now();
    func(matrix);
    endTime = std::chrono::system_clock::now();

    resultTime = (std::chrono::duration_cast<std::chrono::nanoseconds>
            (endTime - startTime).count()) / 1e9;

    currentTime = resultStartTime + resultTime;

    if (needPrinting)
        printf("Task: %3d, Stage: %3d, Start: %.6f, End: %.6f\n",
            task, stage, resultStartTime, resultStartTime + resultTime);
}



void logConway(matrix_t &matrix, int task, int stage, \
    void (*func)(matrix_t &), bool needPrinting) {
    std::chrono::time_point<std::chrono::system_clock> startTime, endTime;
    double resultTime = 0;

    startTime = std::chrono::system_clock::now();
    func(matrix);
    endTime = std::chrono::system_clock::now();

    resultTime = (std::chrono::duration_cast<std::chrono::nanoseconds>
            (endTime - startTime).count()) / 1e9;

    double resultStartTime;

    if (stage == 1) {
        resultStartTime = t1[task - 1];
        t1[task] = resultStartTime + resultTime;
        t2[task - 1] = t1[task];
    } else if (stage == 2) {
        resultStartTime = t2[task - 1];
        t2[task] = resultStartTime + resultTime;
        t3[task - 1] = t2[task];
    } else if (stage == 3) {
        resultStartTime = t3[task - 1];
    }
    if (needPrinting)
        printf("Task: %3d, Stage: %3d, Start: %.6f, End: %.6f\n",
            task, stage, resultStartTime, resultStartTime + resultTime);
}


void stage1Linear(matrix_t &matrix, int task, bool needPrinting) {
    logLinear(matrix, task, 1, getAverage, needPrinting);
}



void stage2Linear(matrix_t &matrix, int task, bool needPrinting) {
    logLinear(matrix, task, 2, getMax, needPrinting);
}


void stage3Linear(matrix_t &matrix, int task, bool needPrinting) {
    logLinear(matrix, task, 3, fillMatrix, needPrinting);
}


void parseLinear(int count, size_t size, bool needPrinting) {
    currentTime = 0;
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    queues_t queues = {.q1 = q1, .q2 = q2, .q3 = q3};

    for (int i = 0; i < count; i++) {
        matrix_t res = generateMatrix(size);

        queues.q1.push(res);
    }

    for (int i = 0; i < count; i++) {
        matrix_t matrix = queues.q1.front();
        stage1Linear(matrix, i + 1, needPrinting);
        queues.q1.pop();
        queues.q2.push(matrix);

        matrix = queues.q2.front();
        stage2Linear(matrix, i + 1, needPrinting);
        queues.q2.pop();
        queues.q3.push(matrix);

        matrix = queues.q3.front();
        stage3Linear(matrix, i + 1, needPrinting);
        queues.q3.pop();
    }
}



void stage1Parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, \
    std::queue<matrix_t> &q3, bool needPrinting) {

    int task = 1;
    std::mutex m;
    while(!q1.empty()) {
        m.lock();
        matrix_t matrix = q1.front();
        m.unlock();

        logConway(matrix, task++, 1, getAverage, needPrinting);

        m.lock();
        q2.push(matrix);
        q1.pop();
        m.unlock();
    }
}


void stage2Parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, \
    std::queue<matrix_t> &q3, bool needPrinting) {

    int task = 1;
    std::mutex m;
    do {
        m.lock();
        bool is_q2empty = q2.empty();
        m.unlock();

        if (!is_q2empty) {
            m.lock();
            matrix_t matrix = q2.front();
            m.unlock();

            logConway(matrix, task++, 2, getMax, needPrinting);

            m.lock();
            q3.push(matrix);
            q2.pop();
            m.unlock();
        }
    } while (!q1.empty() || !q2.empty());
}


void stage3Parallel(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2, \
    std::queue<matrix_t> &q3, bool needPrinting) {

    int task = 1;
    std::mutex m;

    do {
        m.lock();
        bool is_q3empty = q3.empty();
        m.unlock();

        if (!is_q3empty) {
            m.lock();
            matrix_t matrix = q3.front();
            m.unlock();

            logConway(matrix, task++, 3, fillMatrix, needPrinting);

            m.lock();
            q3.pop();
            m.unlock();
        }
    } while (!q1.empty() || !q2.empty() || !q3.empty());
}


void parseParallel(int count, size_t size, bool needPrinting) {
    t1.resize(count + 1);
    t2.resize(count + 1);
    t3.resize(count + 1);

    for (int i = 0; i < count + 1; i++) {
        t1[i] = 0;
        t2[i] = 0;
        t3[i] = 0;
    }

    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    queues_t queues = {.q1 = q1, .q2 = q2, .q3 = q3};


    for (int i = 0; i < count; i++) {
        matrix_t res = generateMatrix(size);
        q1.push(res);
    }

    std::thread threads[THREADS];

    threads[0] = std::thread(stage1Parallel, std::ref(q1), std::ref(q2), std::ref(q3), needPrinting);
    threads[1] = std::thread(stage2Parallel, std::ref(q1), std::ref(q2), std::ref(q3), needPrinting);
    threads[2] = std::thread(stage3Parallel, std::ref(q1), std::ref(q2), std::ref(q3), needPrinting);

    for (int i = 0; i < THREADS; i++) {
        threads[i].join();
    }
}


void timeMessage(void) {
    int option, algOption;

    std::cout << "\nВыбор алгоритма: \
                    \n1) Линейный \
                    \n2) Параллельный\n\n";
    std::cin >> algOption;
    std::cout << "\nЗамер времени: \
                    \n1) Разный размер матриц \
                    \n2) Разное кол-во матриц\n\n";

    std::cin >> option;

    if (option == 1) {
        int count = 0;
        size_t size_b, size_e;
        std::cout << "\nКоличество: ";
        std::cin >> count;
        std::cout << "\nНачальный размер: ";
        std::cin >> size_b;
        std::cout << "\nКонечный размер: ";
        std::cin >> size_e;

        if ((algOption < 3) && (algOption > 0))
            printf("\n\n Размер   |   Время \
                \n----------------------\n");
        else {
            printf("Ошибка: Алгоритм выбран неверно\n");
            return;
        }


        for (size_t i_size = size_b; i_size <= size_e; i_size += STEP_SIZE) {
            currentTime = 0;
            if (algOption == 1) {
                parseLinear(count, i_size, false);
                printf("  %3ld     |   %3.4f\n", i_size, currentTime);
            }
            else if (algOption == 2) {
                parseParallel(count, i_size, false);
                printf("  %3ld     |   %3.4f\n", i_size, currentTime);
            }
        }
    } else if (option == 2) {
        int count_b, count_e;
        size_t size;
        std::cout << "\nНачальное количество: ";
        std::cin >> count_b;
        std::cout << "\nКонечное количество: ";
        std::cin >> count_e;
        std::cout << "\nРазмер: ";
        std::cin >> size;

        if ((algOption < 3) && (algOption > 0))
            printf("\n\n Кол-во   |   Время \
                \n----------------------\n");
        else {
            printf("Ошибка: Алгоритм выбран неверно\n");
            return;
        }


        for (int i_count = count_b; i_count <= count_e; i_count += STEP_COUNT) {
            currentTime = 0;
            if (algOption == 1) {
                parseLinear(i_count, size, false);
                printf("  %4d    |   %3.4f\n", i_count, currentTime);
            }
            else if (algOption == 2) {
                parseParallel(i_count, size, false);
                printf("  %4d    |   %3.4f\n", i_count, currentTime);
            }
        }
    } else {
        printf("Ошибка: Тип замера выбран неварно\n");
    }
}


void stagesInfo() {
    printf("\nПоследовательная обработка матриц: \
            \nЭтап 1. Среднее арифметическое элементов матрицы \
            \nЭтап 2. Максимальный элемент в матрице \
            \nЭтап 3. На нечетную позицию в матрице ставится среднее \
            \n        арифметическое, а на четную - максимальный элемент");
}