#pragma once

#include <random>
#include <vector>
#include <iostream>
#include <queue>
#include <thread>
#include <chrono>
#include <ctime>
#include <mutex>

#include "matrix.h"

#define THREADS 3
#define STEP_SIZE 100
#define STEP_COUNT 5

struct queues_s {
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;
};

using queues_t = struct queues_s;

void parseLinear(int count, size_t size, bool needPrinting);
void parseParallel(int count, size_t size, bool needPrinting);

void timeMessage();
void stagesInfo();
