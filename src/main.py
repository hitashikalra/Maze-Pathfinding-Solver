import pygame
from utils.node import Node, make_grid, draw_grid
from algorithms.astar import astar
from algorithms.dijkstra import dijkstra

# Screen settings
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 50, 50
GRID_SIZE = WIDTH // ROWS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Pathfinding Solver")

def main():
    grid, start, end = make_grid(ROWS, COLS), None, None
    run = True
    while run:
        draw_grid(screen, grid, WIDTH, ROWS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Mouse and keyboard events for start, end, wall placement and algorithm execution go here.
            # Example:
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         astar(start, end, grid)
            #     elif event.key == pygame.K_d:
            #         dijkstra(start, end, grid)
    pygame.quit()

if __name__ == "__main__":
    main()
