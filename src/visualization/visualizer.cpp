#include "visualizer.h"
#include "../utils/node.h"

void drawGrid(sf::RenderWindow& window, Grid& grid, int size) {
    for (int i = 0; i < grid.rows; ++i) {
        for (int j = 0; j < grid.cols; ++j) {
            grid.getNode(i, j)->draw(window, size);
        }
    }
}
