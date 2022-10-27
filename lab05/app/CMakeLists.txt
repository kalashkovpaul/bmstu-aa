cmake_minimum_required(VERSION 3.16)
project(app)

set(CMAKE_CXX_STANDARD 20)
include_directories(include)
add_executable(app main.cpp src/conway.cpp src/matrix.cpp src/menu.cpp src/utils.cpp include/conway.h include/matrix.h include/menu.h include/utils.h)

target_link_libraries(app -lpthread)
