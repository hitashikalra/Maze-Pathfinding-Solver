import heapq
from utils.node import heuristic, reconstruct_path

def astar(start, end, grid):
    open_set = [(0, start)]
    start.cost, start.heuristic = 0, heuristic(start, end)
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            return reconstruct_path(start, end)
        for neighbor in current.neighbors:
            new_cost = current.cost + 1
            if new_cost < neighbor.cost:
                neighbor.cost, neighbor.heuristic = new_cost, new_cost + heuristic(neighbor, end)
                neighbor.parent = current
                heapq.heappush(open_set, (neighbor.heuristic, neighbor))
