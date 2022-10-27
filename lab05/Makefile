CC = g++
FLAGS = -std=c++11 -Wdeprecated
SRC = src/conway.cpp src/matrix.cpp src/menu.cpp src/utils.cpp
INC = include/conway.h include/matrix.h include/menu.h include/utils.h
OUT = app.out

app.out:
	$(CC) main.cpp $(SRC) $(INC) $(FLAGS)

clean:
	rm *.o
