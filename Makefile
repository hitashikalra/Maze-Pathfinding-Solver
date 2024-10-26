CXX = g++
CXXFLAGS = -std=c++11 -Wall
LDFLAGS = -lsfml-graphics -lsfml-window -lsfml-system

SRC = src/main.cpp src/algorithms/astar.cpp src/algorithms/dijkstra.cpp src/utils/node.cpp src/visualization/visualizer.cpp
OBJ = $(SRC:.cpp=.o)
TARGET = MazeSolver

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $(TARGET) $(LDFLAGS)

clean:
	rm -f $(OBJ) $(TARGET)

run: $(TARGET)
	./$(TARGET)
