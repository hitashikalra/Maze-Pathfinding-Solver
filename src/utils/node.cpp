#include "node.h"
#include <cmath>

Node::Node(int r, int c) : row(r), col(c), cost(INFINITY), heuristic(INFINITY), parent(nullptr) {}

void Node::draw(sf::RenderWindow& window, int size) {
    sf::RectangleShape rect(sf::Vector2f(size, size));
    rect.setPosition(row * size, col * size);
    window.draw(rect);
}

Grid::Grid(int r, int c) : rows(r), cols(c) {
    grid.resize(r, std::vector<Node>(c, Node(r, c)));
}

Node* Grid::getNode(int r, int c) {
    return &grid[r][c];
}

std::vector<Node*> reconstructPath(Node* start, Node* end) {
    std::vector<Node*> path;
    Node* current = end;
    while (current != start) {
        path.push_back(current);
        current = current->parent;
    }
    return path;
}
