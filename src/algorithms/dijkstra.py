import heapq
from utils.node import reconstruct_path

def dijkstra(start, end, grid):
    queue = [(0, start)]
    start.cost = 0
    while queue:
        _, current = heapq.heappop(queue)
        if current == end:
            return reconstruct_path(start, end)
        for neighbor in current.neighbors:
            new_cost = current.cost + 1
            if new_cost < neighbor.cost:
                neighbor.cost, neighbor.parent = new_cost, current
                heapq.heappush(queue, (new_cost, neighbor))
