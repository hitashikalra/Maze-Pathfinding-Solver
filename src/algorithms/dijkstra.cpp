#include "algorithms.h"
#include <queue>
#include <cmath>

double heuristic(Node* a, Node* b) {
    return abs(a->row - b->row) + abs(a->col - b->col);
}

std::vector<Node*> astar(Node* start, Node* end, Grid& grid) {
    std::priority_queue<Node*, std::vector<Node*>, CompareNode> openSet;
    start->cost = 0;
    openSet.push(start);

    while (!openSet.empty()) {
        Node* current = openSet.top();
        openSet.pop();

        if (current == end)
            return reconstructPath(start, end);

        for (Node* neighbor : current->neighbors) {
            double newCost = current->cost + 1;
            if (newCost < neighbor->cost) {
                neighbor->cost = newCost;
                neighbor->parent = current;
                neighbor->heuristic = newCost + heuristic(neighbor, end);
                openSet.push(neighbor);
            }
        }
    }

    return {};  // No path found
}
