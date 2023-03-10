import sys, pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0, 0, 0))
pygame.display.flip()
red = (255, 0, 0)
pygame.display.set_caption("Anurag Karki Bresenham Line Drawing Algorithm ")


def bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    slope = dy / dx
    if slope < 1:
        D = 2 * dy - dx
        gfxdraw.pixel(screen, x1, y1, red)
        y = y1

        for x in range(x1 + 1, x2 + 1):
            if D > 0:
                y += 1
                gfxdraw.pixel(screen, x, y, red)
                D -= (2 * dy - 2 * dx)
            else:
                gfxdraw.pixel(screen, x, y, red)
                D += 2 * dy

    elif slope >= 1:
        D = 2 * dx
        gfxdraw.pixel(screen, x1, y1, red)
        x = x1

        for y in range(y1, y2 + 1):
            gfxdraw.pixel(screen, x, y, red)

            D = D + dx
            if (D >= 0):
                x = x + 1
                D = D - 2 * (y2 - y1)
    pygame.display.flip()


bresenham(100, 100, 500, 200)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()