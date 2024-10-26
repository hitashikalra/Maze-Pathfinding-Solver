#ifndef NODE_H
#define NODE_H

#include <vector>
#include <SFML/Graphics.hpp>

class Node {
public:
    int row, col;
    double cost, heuristic;
    Node* parent;
    std::vector<Node*> neighbors;

    Node(int r, int c);

    void draw(sf::RenderWindow& window, int size);
};

class Grid {
public:
    int rows, cols;
    std::vector<std::vector<Node>> grid;

    Grid(int r, int c);
    Node* getNode(int r, int c);
};

std::vector<Node*> reconstructPath(Node* start, Node* end);

#endif
