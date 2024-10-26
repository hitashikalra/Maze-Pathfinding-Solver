import pygame
import math

WHITE, BLACK, GREEN, ORANGE, PURPLE = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 165, 0), (128, 0, 128)

class Node:
    def __init__(self, row, col, grid_size):
        self.row, self.col = row, col
        self.x, self.y = row * grid_size, col * grid_size
        self.color, self.neighbors = WHITE, []
        self.cost, self.heuristic = float('inf'), float('inf')
        self.parent = None
    
    def reset(self): 
        self.color, self.cost, self.heuristic, self.parent = WHITE, float('inf'), float('inf'), None
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, GRID_SIZE, GRID_SIZE))

def heuristic(node1, node2):
    return abs(node1.row - node2.row) + abs(node1.col - node2.col)

def reconstruct_path(start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = current.parent
        current.color = GREEN
    return path[::-1]

def make_grid(rows, cols):
    return [[Node(r, c, GRID_SIZE) for c in range(cols)] for r in range(rows)]
