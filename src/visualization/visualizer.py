import pygame

WHITE, GREY = (255, 255, 255), (128, 128, 128)

def draw_grid(screen, grid, width, rows):
    screen.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(screen)
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0, i * width // rows), (width, i * width // rows))
        pygame.draw.line(screen, GREY, (i * width // rows, 0), (i * width // rows, width))
    pygame.display.flip()
