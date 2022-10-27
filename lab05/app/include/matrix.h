#pragma once

#include <random>
#include <vector>
#include <iostream>
#include <queue>
#include <thread>
#include <math.h>
#include <string>

struct matrix_s {
    std::vector<std::vector<double> > data;
    size_t size;
    double avg;
    double max;
};

using matrix_t = struct matrix_s;

matrix_t generateMatrix(size_t size);
matrix_t copyMatrix(matrix_t matrix);
void printMatrix(matrix_t matrix);

void getAverage(matrix_t &matrix);
void getMax(matrix_t &matrix);
void fillMatrix(matrix_t &matrix);
