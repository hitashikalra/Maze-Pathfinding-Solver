#include <SFML/Graphics.hpp>
#include "utils/node.h"
#include "algorithms/algorithms.h"
#include "visualization/visualizer.h"

const int WIDTH = 800;
const int HEIGHT = 800;
const int ROWS = 50;

int main() {
    sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "Maze Pathfinding Solver");

    Grid grid(ROWS, ROWS);
    Node* start = nullptr;
    Node* end = nullptr;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
            // Add event handling for setting start, end, and wall nodes
        }
        window.clear(sf::Color::White);
        drawGrid(window, grid, ROWS);
        window.display();
    }

    return 0;
}
