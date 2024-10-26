#ifndef ALGORITHMS_H
#define ALGORITHMS_H

#include <vector>
#include "../utils/node.h"

std::vector<Node*> astar(Node* start, Node* end, Grid& grid);
std::vector<Node*> dijkstra(Node* start, Node* end, Grid& grid);

#endif
